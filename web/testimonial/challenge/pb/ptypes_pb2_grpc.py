# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ptypes_pb2 as ptypes__pb2


class RickyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubmitTestimonial = channel.unary_unary(
                '/RickyService/SubmitTestimonial',
                request_serializer=ptypes__pb2.TestimonialSubmission.SerializeToString,
                response_deserializer=ptypes__pb2.GenericReply.FromString,
                )


class RickyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SubmitTestimonial(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RickyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubmitTestimonial': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitTestimonial,
                    request_deserializer=ptypes__pb2.TestimonialSubmission.FromString,
                    response_serializer=ptypes__pb2.GenericReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RickyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RickyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SubmitTestimonial(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RickyService/SubmitTestimonial',
            ptypes__pb2.TestimonialSubmission.SerializeToString,
            ptypes__pb2.GenericReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
