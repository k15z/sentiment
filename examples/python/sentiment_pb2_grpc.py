# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import sentiment_pb2 as sentiment__pb2


class SentimentStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Analyze = channel.unary_unary(
        '/sentiment.Sentiment/Analyze',
        request_serializer=sentiment__pb2.SentimentRequest.SerializeToString,
        response_deserializer=sentiment__pb2.SentimentReply.FromString,
        )
    self.AnalyzeStream = channel.stream_stream(
        '/sentiment.Sentiment/AnalyzeStream',
        request_serializer=sentiment__pb2.SentimentRequest.SerializeToString,
        response_deserializer=sentiment__pb2.SentimentReply.FromString,
        )


class SentimentServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Analyze(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AnalyzeStream(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SentimentServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Analyze': grpc.unary_unary_rpc_method_handler(
          servicer.Analyze,
          request_deserializer=sentiment__pb2.SentimentRequest.FromString,
          response_serializer=sentiment__pb2.SentimentReply.SerializeToString,
      ),
      'AnalyzeStream': grpc.stream_stream_rpc_method_handler(
          servicer.AnalyzeStream,
          request_deserializer=sentiment__pb2.SentimentRequest.FromString,
          response_serializer=sentiment__pb2.SentimentReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sentiment.Sentiment', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
