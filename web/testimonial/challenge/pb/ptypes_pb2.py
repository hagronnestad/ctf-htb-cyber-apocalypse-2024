# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ptypes.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cptypes.proto\">\n\x15TestimonialSubmission\x12\x10\n\x08\x63ustomer\x18\x01 \x01(\t\x12\x13\n\x0btestimonial\x18\x02 \x01(\t\"\x1f\n\x0cGenericReply\x12\x0f\n\x07message\x18\x01 \x01(\t2L\n\x0cRickyService\x12<\n\x11SubmitTestimonial\x12\x16.TestimonialSubmission\x1a\r.GenericReply\"\x00\x42\x05Z\x03/pbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ptypes_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\003/pb'
  _globals['_TESTIMONIALSUBMISSION']._serialized_start=16
  _globals['_TESTIMONIALSUBMISSION']._serialized_end=78
  _globals['_GENERICREPLY']._serialized_start=80
  _globals['_GENERICREPLY']._serialized_end=111
  _globals['_RICKYSERVICE']._serialized_start=113
  _globals['_RICKYSERVICE']._serialized_end=189
# @@protoc_insertion_point(module_scope)
