import pytest


SAMPLE_FILES = [
    'data/canada.json',
    'data/citm_catalog.json',
    'data/twitter.json',
    'data/verysmall.json'
]


@pytest.fixture(params=SAMPLE_FILES, scope='module')
def sample_json(request):
    # We pass in the complete file contents, because we don't want file IO
    # to skew results.
    with open(request.param) as src:
        yield request.param, src.read()


@pytest.fixture(params=SAMPLE_FILES, scope='module')
def sample_json_bytes(request):
    # Streaming/SAX parsers consume bytes. As above, the whole file is read
    # into memory up front so file IO doesn't skew the parse benchmark.
    with open(request.param, 'rb') as src:
        yield request.param, src.read()
