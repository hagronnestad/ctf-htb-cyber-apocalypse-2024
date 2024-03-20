import sys

import grpc
# Import the generated classes
import ptypes_pb2
import ptypes_pb2_grpc

# Create a channel to connect to the server.
channel = grpc.insecure_channel('localhost:50045')

# Create a stub (client)
stub = ptypes_pb2_grpc.RickyServiceStub(channel)

# If sys.argv[2] is a path to any existing file read the file into a variable
with open(sys.argv[2], 'r') as file:
    file = file.read()


# Create a request object
request = ptypes_pb2.TestimonialSubmission(
    customer=sys.argv[1], testimonial=file
)

# Make the call
response = stub.SubmitTestimonial(request)

# Print the response
print(response.message)
