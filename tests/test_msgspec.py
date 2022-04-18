import pytest

msgspec = pytest.importorskip('msgspec')

dec = msgspec.json.Decoder()


def parse_document(path, content):
    dec.decode(content)


def test_full_document_read(benchmark, sample_json):
    """
    Benchmarks the performance of completely reading in a document to a Python
    object.
    """
    path, content = sample_json
    content = content.encode("utf-8")
    benchmark.group = f'Complete load of {path}'
    benchmark.name = 'msgspec'
    benchmark.extra_info['file'] = path
    benchmark.extra_info['file_size'] = len(content)
    benchmark(parse_document, path, content)
