import pytest

json_merge_patch = pytest.importorskip('json_merge_patch')


def merge_patch(patch):
    json_merge_patch.merge({'a': 1}, patch)


def test_merge_patch(benchmark):
    benchmark.group = 'Merge Patch'
    benchmark.name = 'json_merge_patch'

    patch = {'a': 3, 'b': 5}

    benchmark(merge_patch, patch)
