import json


def parse_document(path, content):
    json.loads(content)


def test_full_document_read(benchmark, sample_json):
    """
    Benchmarks the performance of completely reading in a document to a Python
    object.
    """
    benchmark.group = f'Complete load of {sample_json[0]}'
    benchmark.name = 'json'
    benchmark(parse_document, *sample_json)
