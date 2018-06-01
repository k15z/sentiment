# sentiment
Neural sentiment analysis over gRPC.

## usage
Run `python server.py` to launch an instance of the gRPC server. The only dependencies
are `pytorch` and `grpc` and the server defaults to port 50051.

The `examples` directory shows how to interact with the gRPC API from both Python and 
Go. An abbreviated example is provided below:

```
import grpc
import sentiment_pb2 as sentiment_pb2
import sentiment_pb2_grpc as sentiment_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = sentiment_pb2_grpc.SentimentStub(channel)

text = "The display resolution is fantastic and the speakers are crisp and clear."
result = stub.Analyze(sentiment_pb2.SentimentRequest(text=text))

print("Positive:", result.positive)
print("Negative:", result.negative)
```
