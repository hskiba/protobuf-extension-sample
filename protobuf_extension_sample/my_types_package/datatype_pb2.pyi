from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[DataType]
    ARRAY: _ClassVar[DataType]
    BOOL: _ClassVar[DataType]
    CHAR: _ClassVar[DataType]
    DATE: _ClassVar[DataType]
    DATETIME: _ClassVar[DataType]
    INT: _ClassVar[DataType]
    NUM: _ClassVar[DataType]
UNKNOWN: DataType
ARRAY: DataType
BOOL: DataType
CHAR: DataType
DATE: DataType
DATETIME: DataType
INT: DataType
NUM: DataType
MY_DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
my_data_type: _descriptor.FieldDescriptor
