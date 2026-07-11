import pytest

parser = pytest.importorskip('yyjson')


def parse_document(_, content):
    parser.loads(content)


def test_full_document_read(benchmark, sample_json):
    """
    Benchmarks the performance of completely reading in a document to a Python
    object.
    """
    benchmark.group = f'Complete load of {sample_json[0]}'
    benchmark.name = 'yyjson'
    benchmark.extra_info['file'] = sample_json[0]
    benchmark.extra_info['file_size'] = len(sample_json[1])
    benchmark(parse_document, *sample_json)


class _Visitor:
    """A SAX handler that visits every token (each event crosses into Python,
    matching what ``ijson`` does when it yields every event)."""

    def obj_begin(self): pass
    def obj_end(self, count): pass
    def arr_begin(self): pass
    def arr_end(self, count): pass
    def key(self, value): pass
    def string(self, value): pass
    def number(self, value): pass
    def boolean(self, value): pass
    def null(self): pass


def parse_streaming(_, content):
    parser.sax(content, _Visitor())


def test_streaming_read(benchmark, sample_json_bytes):
    """
    Benchmarks bounded-memory streaming: every JSON token is dispatched to a
    Python handler without ever building the full document. Compare against
    ``ijson`` in the same group.
    """
    benchmark.group = f'Streaming parse of {sample_json_bytes[0]}'
    benchmark.name = 'yyjson'
    benchmark.extra_info['file'] = sample_json_bytes[0]
    benchmark.extra_info['file_size'] = len(sample_json_bytes[1])
    benchmark(parse_streaming, *sample_json_bytes)


def merge_patch(patch, document):
    document.patch(patch, use_merge_patch=True)


def test_merge_patch(benchmark):
    benchmark.group = 'Merge Patch'
    benchmark.name = 'yyjson'

    patch = parser.Document({'a': 3, 'b': 5})
    document = parser.Document({'a': 1})

    benchmark(merge_patch, patch, document)
