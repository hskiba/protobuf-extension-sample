from protobuf_extension_sample.my_types_package import datatype_pb2 as _datatype_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Sample(_message.Message):
    __slots__ = ("Bool", "Num", "Date", "Datetime", "Int", "Array", "Char", "Unsupported")
    BOOL_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    INT_FIELD_NUMBER: _ClassVar[int]
    ARRAY_FIELD_NUMBER: _ClassVar[int]
    CHAR_FIELD_NUMBER: _ClassVar[int]
    UNSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    Bool: bool
    Num: float
    Date: int
    Datetime: int
    Int: int
    Array: _containers.RepeatedScalarFieldContainer[float]
    Char: str
    Unsupported: int
    def __init__(self, Bool: bool = ..., Num: _Optional[float] = ..., Date: _Optional[int] = ..., Datetime: _Optional[int] = ..., Int: _Optional[int] = ..., Array: _Optional[_Iterable[float]] = ..., Char: _Optional[str] = ..., Unsupported: _Optional[int] = ...) -> None: ...
