import pytest


SAMPLE_FILES = [
    'data/canada.json',
    'data/citm_catalog.json',
    'data/twitter.json',
    'data/verysmall.json',
    # From the yyjson_benchmark corpus (github.com/ibireme/yyjson_benchmark):
    # two genuinely large documents plus two mid-size ones that add shape
    # diversity (poet.json is CJK-string-heavy).
    'data/fgo.json',
    'data/otfcc.json',
    'data/poet.json',
    'data/gsoc-2018.json',
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
