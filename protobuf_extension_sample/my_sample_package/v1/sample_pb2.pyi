from protobuf_extension_sample.my_types_package.v1 import datatype_pb2 as _datatype_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Sample(_message.Message):
    __slots__ = ("bool", "num", "date", "datetime", "int", "array", "char", "unsupported")
    BOOL_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    INT_FIELD_NUMBER: _ClassVar[int]
    ARRAY_FIELD_NUMBER: _ClassVar[int]
    CHAR_FIELD_NUMBER: _ClassVar[int]
    UNSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    bool: bool
    num: float
    date: int
    datetime: int
    int: int
    array: _containers.RepeatedScalarFieldContainer[float]
    char: str
    unsupported: int
    def __init__(self, bool: bool = ..., num: _Optional[float] = ..., date: _Optional[int] = ..., datetime: _Optional[int] = ..., int: _Optional[int] = ..., array: _Optional[_Iterable[float]] = ..., char: _Optional[str] = ..., unsupported: _Optional[int] = ...) -> None: ...
