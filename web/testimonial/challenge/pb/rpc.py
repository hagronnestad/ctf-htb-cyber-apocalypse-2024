import sys

import grpc
# Import the generated classes
import ptypes_pb2
import ptypes_pb2_grpc

# Create a channel to connect to the server.
channel = grpc.insecure_channel('0.0.0.0:50045')

# Create a stub (client)
stub = ptypes_pb2_grpc.RickyServiceStub(channel)

# Create a request object
request = ptypes_pb2.TestimonialSubmission(
    customer=sys.argv[1], testimonial=sys.argv[2] + '\n'
)

# Make the call
response = stub.SubmitTestimonial(request)

# Print the response
print(response.message)
