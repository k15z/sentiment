"""
This script loads and serves a sentiment analysis model over gRPC.
"""
import torch
import torch.nn as nn
import torch.nn.functional as F

C = torch.load("resources/bytepairs.pt")
def text_to_tensor(text):
    x = []
    text = text.lower()
    while len(text) > 0:
        if text[:3] in C:
            x.append(C[text[:3]])
            text = text[3:]
            continue
        if text[:2] in C:
            x.append(C[text[:2]])
            text = text[2:]
            continue
        if text[0] in C:
            x.append(C[text[0]])
        text = text[1:]
    return torch.LongTensor(x)

class BasicSentiment(nn.Module):

    def __init__(self, num_embeddings, hidden_dim, output_dim):
        super(BasicSentiment, self).__init__()
        self.embed = nn.Embedding(num_embeddings, hidden_dim)
        self.encode = nn.GRU(hidden_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.linear = nn.Linear(hidden_dim*4, output_dim)

    def forward(self, x):
        x = self.embed(x)
        x, _ = self.encode(x)
        x1, _ = torch.max(x, dim=1)
        x2, _ = torch.min(x, dim=1)
        x = self.linear(torch.cat([x1, x2], dim=1))
        return x

#--------------------------------------------------------------------------------

import grpc, time
import sentiment_pb2 as sentiment_pb2
import sentiment_pb2_grpc as sentiment_pb2_grpc
from concurrent import futures

class BasicSentimentWrapper(object):

    def __init__(self, path_to_model):
        model = BasicSentiment(num_embeddings=len(C)+1, hidden_dim=64, output_dim=2)
        model.load_state_dict(torch.load(path_to_model))
        self.model = model

    def predict(self, text):
        pred = self.model(text_to_tensor(text).unsqueeze(0))[0]
        pred = F.softmax(pred, dim=0).detach().numpy().tolist()
        return {"negative": pred[0], "positive": pred[1]}

class SentimentServicer(sentiment_pb2_grpc.SentimentServicer):

    def __init__(self):
        self.model = BasicSentimentWrapper("resources/weights.pt")

    def Analyze(self, request, context):
        pred = self.model.predict(request.text)
        return sentiment_pb2.SentimentReply(positive=pred["positive"], negative=pred["negative"])

    def AnalyzeStream(self, requests, context):
        for request in requests:
            pred = self.model.predict(request.text)
            yield sentiment_pb2.SentimentReply(positive=pred["positive"], negative=pred["negative"])

#--------------------------------------------------------------------------------

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    sentiment_pb2_grpc.add_SentimentServicer_to_server(SentimentServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
