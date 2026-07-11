import pytest

ijson = pytest.importorskip('ijson')


def parse_streaming(_, content):
    # `basic_parse` is ijson's lowest-level event stream (no JSON-path
    # tracking), the closest analog to a SAX handler. `use_float=True` makes it
    # yield native floats instead of Decimals, matching yyjson.sax's default so
    # the two are compared doing equal work. ijson accepts bytes directly.
    for _event in ijson.basic_parse(content, use_float=True):
        pass


def test_streaming_read(benchmark, sample_json_bytes):
    """
    Benchmarks streaming parse throughput using ijson's C (yajl2) backend.
    Shares the 'Streaming parse of ...' group with yyjson's SAX reader.
    """
    benchmark.group = f'Streaming parse of {sample_json_bytes[0]}'
    benchmark.name = f'ijson ({ijson.backend})'
    benchmark.extra_info['file'] = sample_json_bytes[0]
    benchmark.extra_info['file_size'] = len(sample_json_bytes[1])
    benchmark.extra_info['backend'] = ijson.backend
    benchmark(parse_streaming, *sample_json_bytes)
