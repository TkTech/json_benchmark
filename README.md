# json_benchmark

<!-- start_last_updated_block -->


> :grey_exclamation: Benchmarks regenerated on 2023-09-05

<!-- end_last_updated_block -->


This repository contains benchmarks for **Python** JSON readers & writers.
What's the fastest Python JSON parser? Let's find out.

To run the tests yourself:

```bash
git clone git@github.com:TkTech/json_benchmark.git && cd json_benchmark
<setup a virtualenv using your tool of choice>
poetry install
pytest --benchmark-json benchmark.json --benchmark-histogram histograms/
```

To update the tables in the README.md with the new results, just run:

```
python generate_benchmark_summaries.py
python generate_minefield_reports.py
```

## Candidate Libraries

The following libraries are the current candidates for benchmarking. Feel free
to request or add new libraries.

| Library    | Reader | Writer | Version |
|------------|--------|--------|---------|
| simdjson   | Yes    | No     | 6.0.0   |
| cysimdjson | Yes    | No     | 23.9    |
| yyjson     | Yes    | Yes    | 2.3.1   |
| orjson     | Yes    | Yes    | 3.9.5   |
| rapidjson  | Yes    | Yes    | 1.10    |
| ujson      | Yes    | Yes    | 5.8.0   |
| json       | Yes    | Yes    | 3.11    |
| msgspec    | Yes    | Yes    | 0.18.2  |

## Correctness

cd
It doesn't matter how fast a JSON parser is if it's not going to give you the
correct results. We run the JSON minefield against each library. To see the
complete line-by-line results, see the <minefield_reports/>
directory.

<!-- start_correct_block -->


### yyjson

See full minefield results for [yyjson](minefield_reports/yyjson.md).

| count | result |
| ----- | ------ |
| 283 | 🎉 expected result |
| 0 | 🔥 parsing should have failed but succeeded |
| 0 | 🔥 parsing should have succeeded but failed |
| 6 | ➕ result undefined, parsing succeeded |
| 29 | ➖ result undefined, parsing failed |

### rapidjson

See full minefield results for [rapidjson](minefield_reports/rapidjson.md).

| count | result |
| ----- | ------ |
| 277 | 🎉 expected result |
| 6 | 🔥 parsing should have failed but succeeded |
| 0 | 🔥 parsing should have succeeded but failed |
| 6 | ➕ result undefined, parsing succeeded |
| 29 | ➖ result undefined, parsing failed |

### orjson

See full minefield results for [orjson](minefield_reports/orjson.md).

| count | result |
| ----- | ------ |
| 283 | 🎉 expected result |
| 0 | 🔥 parsing should have failed but succeeded |
| 0 | 🔥 parsing should have succeeded but failed |
| 6 | ➕ result undefined, parsing succeeded |
| 29 | ➖ result undefined, parsing failed |

### simdjson

See full minefield results for [simdjson](minefield_reports/simdjson.md).

| count | result |
| ----- | ------ |
| 283 | 🎉 expected result |
| 0 | 🔥 parsing should have failed but succeeded |
| 0 | 🔥 parsing should have succeeded but failed |
| 3 | ➕ result undefined, parsing succeeded |
| 32 | ➖ result undefined, parsing failed |

### ujson

See full minefield results for [ujson](minefield_reports/ujson.md).

| count | result |
| ----- | ------ |
| 267 | 🎉 expected result |
| 16 | 🔥 parsing should have failed but succeeded |
| 0 | 🔥 parsing should have succeeded but failed |
| 21 | ➕ result undefined, parsing succeeded |
| 14 | ➖ result undefined, parsing failed |

### msgspec

See full minefield results for [msgspec](minefield_reports/msgspec.md).

| count | result |
| ----- | ------ |
| 283 | 🎉 expected result |
| 0 | 🔥 parsing should have failed but succeeded |
| 0 | 🔥 parsing should have succeeded but failed |
| 6 | ➕ result undefined, parsing succeeded |
| 29 | ➖ result undefined, parsing failed |

<!-- end_correct_block -->


## Performance

In these benchmarks, lower is better.

<!-- start_performance_block -->


### Complete load of data/canada.json

Sample file is 2251051 bytes.

![](histograms/-Complete_load_of_data_canada.json.svg 'Histogram for Complete load of data/canada.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| orjson | 5.0019 | 14.1927 | 9.6857 |
| simdjson | 5.8214 | 18.1483 | 11.5799 |
| msgspec | 5.9027 | 16.1104 | 10.1492 |
| cysimdjson | 5.9696 | 14.7102 | 9.1315 |
| yyjson | 6.1175 | 21.2752 | 12.7247 |
| ujson | 10.1714 | 24.2481 | 16.5537 |
| json | 21.6314 | 30.1396 | 26.0608 |
| rapidjson | 23.4999 | 34.4533 | 29.2562 |


### Complete load of data/citm_catalog.json

Sample file is 1727030 bytes.

![](histograms/-Complete_load_of_data_citm_catalog.json.svg 'Histogram for Complete load of data/citm_catalog.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| orjson | 2.2511 | 12.9107 | 3.9478 |
| yyjson | 2.7017 | 17.0122 | 5.3347 |
| simdjson | 2.8785 | 15.3378 | 5.0631 |
| msgspec | 2.9459 | 13.9166 | 4.5182 |
| cysimdjson | 3.0251 | 8.7956 | 4.0554 |
| rapidjson | 4.7612 | 15.9753 | 6.7336 |
| ujson | 4.8497 | 19.4423 | 7.4472 |
| json | 4.9647 | 11.9016 | 6.2808 |


### Complete load of data/twitter.json

Sample file is 567916 bytes.

![](histograms/-Complete_load_of_data_twitter.json.svg 'Histogram for Complete load of data/twitter.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| orjson | 0.8254 | 9.2997 | 0.9887 |
| yyjson | 0.9115 | 13.4172 | 1.1653 |
| simdjson | 0.9708 | 11.7451 | 1.1930 |
| msgspec | 1.0621 | 10.1093 | 1.2256 |
| cysimdjson | 1.3525 | 7.0623 | 1.4850 |
| rapidjson | 2.0156 | 12.0504 | 2.2450 |
| json | 2.1043 | 9.7267 | 2.2753 |
| ujson | 2.2015 | 14.4491 | 2.4740 |


### Complete load of data/verysmall.json

Sample file is 7 bytes.

![](histograms/-Complete_load_of_data_verysmall.json.svg 'Histogram for Complete load of data/verysmall.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| msgspec | 0.0001 | 0.0003 | 0.0001 |
| orjson | 0.0001 | 0.0003 | 0.0001 |
| simdjson | 0.0002 | 0.0008 | 0.0002 |
| ujson | 0.0002 | 0.0011 | 0.0003 |
| rapidjson | 0.0003 | 0.0015 | 0.0003 |
| yyjson | 0.0003 | 0.0014 | 0.0003 |
| cysimdjson | 0.0003 | 0.0009 | 0.0003 |
| json | 0.0007 | 0.0019 | 0.0007 |


### Merge Patch

![](histograms/-Merge_Patch.svg 'Histogram for Merge Patch.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 0.0004 | 0.0010 | 0.0004 |
| json_merge_patch | 0.0004 | 0.0027 | 0.0005 |


<!-- end_performance_block -->


## FAQ

### Why doesn't this run benchmarks using Github Actions?

Generally, unless you control the CI runners with self-hosted boxes (which are
unsafe on public Github projects!), you have no idea what machine you're going
to get, or how many *other* jobs may be running on the same machine. This can
cause the benchmarks to vary drastically between runs, even minutes apart. For
this reason benchmarks are always run locally on a consistent machine, in a
consistent state.

### What machine is used for the x64 benchmarks?

x64 tests are run on an AMD Ryzen 7 5800X, capped at base clock speed with
64GB of Corsair CMW32GX4M2E3200C16.

### JSON is terrible, use X!

This repository isn't for arguing the pros or cons of JSON versus some other
exchange format. You frequently have no choice but to work with JSON, and if
you can read or write responses 15% faster, that means you can handle more
requests per second with the same hardware.

