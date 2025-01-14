# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto

from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import reflection as _reflection
from google.protobuf import message as _message
from google.protobuf import descriptor as _descriptor
import sys
_b = sys.version_info[0] < 3 and (
    lambda x: x) or (lambda x: x.encode('latin1'))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='data.proto',
    package='api',
    syntax='proto3',
    serialized_options=_b('P\001'),
    serialized_pb=_b('\n\ndata.proto\x12\x03\x61pi\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"$\n\x03Row\x12\x1d\n\x07\x43olumns\x18\x01 \x03(\x0b\x32\x0c.api.DBValue\"\x99\x02\n\x07\x44\x42Value\x12\x14\n\nInt32Value\x18\x01 \x01(\x05H\x00\x12\x14\n\nInt64Value\x18\x02 \x01(\x03H\x00\x12\x16\n\x0c\x46loat32Value\x18\x05 \x01(\x02H\x00\x12\x16\n\x0c\x46loat64Value\x18\x06 \x01(\x01H\x00\x12\x15\n\x0bStringValue\x18\x07 \x01(\tH\x00\x12\x14\n\nBytesValue\x18\x08 \x01(\x0cH\x00\x12\x34\n\x0eTimeStampValue\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x12/\n\tNullValue\x18\x0b \x01(\x0e\x32\x1a.google.protobuf.NullValueH\x00\x12\x14\n\nOtherValue\x18\x0c \x01(\tH\x00\x42\x08\n\x06\x44\x42TypeB\x02P\x01\x62\x06proto3'),
    dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR, google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR, ])


_ROW = _descriptor.Descriptor(
    name='Row',
    full_name='api.Row',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='Columns', full_name='api.Row.Columns', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=82,
    serialized_end=118,
)


_DBVALUE = _descriptor.Descriptor(
    name='DBValue',
    full_name='api.DBValue',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='Int32Value', full_name='api.DBValue.Int32Value', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='Int64Value', full_name='api.DBValue.Int64Value', index=1,
            number=2, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='Float32Value', full_name='api.DBValue.Float32Value', index=2,
            number=5, type=2, cpp_type=6, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='Float64Value', full_name='api.DBValue.Float64Value', index=3,
            number=6, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='StringValue', full_name='api.DBValue.StringValue', index=4,
            number=7, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='BytesValue', full_name='api.DBValue.BytesValue', index=5,
            number=8, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='TimeStampValue', full_name='api.DBValue.TimeStampValue', index=6,
            number=10, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='NullValue', full_name='api.DBValue.NullValue', index=7,
            number=11, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='OtherValue', full_name='api.DBValue.OtherValue', index=8,
            number=12, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name='DBType', full_name='api.DBValue.DBType',
            index=0, containing_type=None, fields=[]),
    ],
    serialized_start=121,
    serialized_end=402,
)

_ROW.fields_by_name['Columns'].message_type = _DBVALUE
_DBVALUE.fields_by_name['TimeStampValue'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DBVALUE.fields_by_name['NullValue'].enum_type = google_dot_protobuf_dot_struct__pb2._NULLVALUE
_DBVALUE.oneofs_by_name['DBType'].fields.append(
    _DBVALUE.fields_by_name['Int32Value'])
_DBVALUE.fields_by_name['Int32Value'].containing_oneof = _DBVALUE.oneofs_by_name['DBType']
_DBVALUE.oneofs_by_name['DBType'].fields.append(
    _DBVALUE.fields_by_name['Int64Value'])
_DBVALUE.fields_by_name['Int64Value'].containing_oneof = _DBVALUE.oneofs_by_name['DBType']
_DBVALUE.oneofs_by_name['DBType'].fields.append(
    _DBVALUE.fields_by_name['Float32Value'])
_DBVALUE.fields_by_name['Float32Value'].containing_oneof = _DBVALUE.oneofs_by_name['DBType']
_DBVALUE.oneofs_by_name['DBType'].fields.append(
    _DBVALUE.fields_by_name['Float64Value'])
_DBVALUE.fields_by_name['Float64Value'].containing_oneof = _DBVALUE.oneofs_by_name['DBType']
_DBVALUE.oneofs_by_name['DBType'].fields.append(
    _DBVALUE.fields_by_name['StringValue'])
_DBVALUE.fields_by_name['StringValue'].containing_oneof = _DBVALUE.oneofs_by_name['DBType']
_DBVALUE.oneofs_by_name['DBType'].fields.append(
    _DBVALUE.fields_by_name['BytesValue'])
_DBVALUE.fields_by_name['BytesValue'].containing_oneof = _DBVALUE.oneofs_by_name['DBType']
_DBVALUE.oneofs_by_name['DBType'].fields.append(
    _DBVALUE.fields_by_name['TimeStampValue'])
_DBVALUE.fields_by_name['TimeStampValue'].containing_oneof = _DBVALUE.oneofs_by_name['DBType']
_DBVALUE.oneofs_by_name['DBType'].fields.append(
    _DBVALUE.fields_by_name['NullValue'])
_DBVALUE.fields_by_name['NullValue'].containing_oneof = _DBVALUE.oneofs_by_name['DBType']
_DBVALUE.oneofs_by_name['DBType'].fields.append(
    _DBVALUE.fields_by_name['OtherValue'])
_DBVALUE.fields_by_name['OtherValue'].containing_oneof = _DBVALUE.oneofs_by_name['DBType']
DESCRIPTOR.message_types_by_name['Row'] = _ROW
DESCRIPTOR.message_types_by_name['DBValue'] = _DBVALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), {
    'DESCRIPTOR': _ROW,
    '__module__': 'data_pb2'
    # @@protoc_insertion_point(class_scope:api.Row)
})
_sym_db.RegisterMessage(Row)

DBValue = _reflection.GeneratedProtocolMessageType('DBValue', (_message.Message,), {
    'DESCRIPTOR': _DBVALUE,
    '__module__': 'data_pb2'
    # @@protoc_insertion_point(class_scope:api.DBValue)
})
_sym_db.RegisterMessage(DBValue)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
