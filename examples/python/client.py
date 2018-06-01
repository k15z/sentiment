"""
This script shows how to use the sentiment analysis model. 
"""
import grpc
import sentiment_pb2 as sentiment_pb2
import sentiment_pb2_grpc as sentiment_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = sentiment_pb2_grpc.SentimentStub(channel)

# basic usage
text = "The display resolution is fantastic and the speakers are crisp and clear."
result = stub.Analyze(sentiment_pb2.SentimentRequest(text=text))
print(result.positive, result.negative)

# iterator usage
def iterate():
	for text in ["Good morning!", "This is terrible."]:
		yield sentiment_pb2.SentimentRequest(text=text)
for result in stub.AnalyzeStream(iterate()):
	print(result.positive, result.negative)
