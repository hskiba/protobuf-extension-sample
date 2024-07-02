from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_TYPE_UNSPECIFIED: _ClassVar[DataType]
    DATA_TYPE_ARRAY: _ClassVar[DataType]
    DATA_TYPE_BOOL: _ClassVar[DataType]
    DATA_TYPE_CHAR: _ClassVar[DataType]
    DATA_TYPE_DATE: _ClassVar[DataType]
    DATA_TYPE_DATETIME: _ClassVar[DataType]
    DATA_TYPE_INT: _ClassVar[DataType]
    DATA_TYPE_NUM: _ClassVar[DataType]
DATA_TYPE_UNSPECIFIED: DataType
DATA_TYPE_ARRAY: DataType
DATA_TYPE_BOOL: DataType
DATA_TYPE_CHAR: DataType
DATA_TYPE_DATE: DataType
DATA_TYPE_DATETIME: DataType
DATA_TYPE_INT: DataType
DATA_TYPE_NUM: DataType
MY_DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
my_data_type: _descriptor.FieldDescriptor
