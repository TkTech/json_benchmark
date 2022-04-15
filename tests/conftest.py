import pytest


@pytest.fixture(params=[
    'data/canada.json',
    'data/citm_catalog.json',
    'data/twitter.json'
], scope='module')
def sample_json(request):
    # We pass in the complete file contents, because we don't want file IO
    # to skew results.
    with open(request.param) as src:
        yield request.param, src.read()
