import pytest

parser = pytest.importorskip('simdjson')


def parse_document(p, document, path, content):
    doc = p.parse(content, document)
    doc.as_object


def test_full_document_read(benchmark, sample_json):
    """
    Benchmarks the performance of completely reading in a document to a Python
    object.
    """
    benchmark.group = f'Complete load of {sample_json[0]}'
    benchmark.name = 'simdjson'
    benchmark.extra_info['file'] = sample_json[0]
    benchmark.extra_info['file_size'] = len(sample_json[1])
    p = parser.Parser()
    document = parser.Document()
    benchmark(parse_document, p, document, *sample_json)
