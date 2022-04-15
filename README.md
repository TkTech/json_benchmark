# json_benchmark

This repository contains benchmarks for **Python** JSON readers & writers.

To run the tests yourself:

```bash
git clone git@github.com:TkTech/json_benchmark.git && cd json_benchmark
<setup a virtualenv using your tool of choice>
pip install -r requirements.txt
pytest
```

## Candidate Libraries

The following libraries are the current candidates for benchmarking. Feel free
to request or add new libraries.

| Library    | Reader | Writer | Version |
|------------|--------|--------|---------|
| simdjson   | Yes    | No     | 4.0.3   |
| cysimdjson | Yes    | No     | 21.11   |
| yyjson     | Yes    | Yes    | 1.0.0   |
| orjson     | Yes    | Yes    | 3.6.7   |
| rapidjson  | Yes    | Yes    | 1.6     |
| ujson      | Yes    | Yes    | 5.2.0   |
| json       | Yes    | Yes    | 3.10    |


## Correctness

It doesn't matter how fast a JSON parser is if it's not going to give you the
correct results. We run the JSON minefield against each library. To see the
complete line-by-line results, see the [minefield_reports/](minefield_reports/)
directory.

[//]: # (start_correct)
[//]: # (end_correct)


## FAQ

### Why doesn't this run benchmarks using Github Actions?

Generally, unless you control the CI runners with self-hosted boxes (which are
unsafe on public Github projects!), you have no idea what machine you're going
to get, or how many _other_ jobs may be running on the same machine. This can
cause the benchmarks to vary drastically between runs, even minutes apart. For
this reason benchmarks are always run locally on a consistent machine, in a
consistent state.

### What machine is used for the x64 benchmarks?

x64 tests are run on an AMD Ryzen 7 5800X, capped at base clock speed with
64GB of Corsair CMW32GX4M2E3200C16.