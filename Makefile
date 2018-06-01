all:
	python -m grpc_tools.protoc -I=./resources --python_out=. --grpc_python_out=. sentiment.proto

clean:
	rm sentiment_pb*
