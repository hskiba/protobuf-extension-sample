clean:
	find . -path './venv' -prune -o -name '*_pb2.py' -type f -exec rm {} \;
	find . -path './venv' -prune -o -name '*_pb2.pyi' -type f -exec rm {} \;

buf: clean
	protoc -I=. --python_out=. --pyi_out=. protobuf_extension_sample/my_sample_package/v1/sample.proto protobuf_extension_sample/my_types_package/v1/datatype.proto
