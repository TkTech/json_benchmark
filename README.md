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
| orjson | 4.9561 | 16.6607 | 10.0456 |
| msgspec | 5.7846 | 16.6313 | 10.4164 |
| simdjson | 5.8509 | 18.2607 | 11.8949 |
| cysimdjson | 5.8934 | 13.6610 | 9.2341 |
| yyjson | 6.1859 | 20.9625 | 13.0847 |
| ujson | 10.1161 | 25.8113 | 16.7394 |
| json | 21.5586 | 29.5351 | 25.5261 |
| rapidjson | 23.2912 | 35.8780 | 29.4905 |

### Complete load of data/citm_catalog.json

Sample file is 1727030 bytes.

![](histograms/-Complete_load_of_data_citm_catalog.json.svg 'Histogram for Complete load of data/citm_catalog.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| orjson | 2.2132 | 13.0309 | 4.0447 |
| yyjson | 2.6798 | 16.9011 | 5.3773 |
| simdjson | 2.8619 | 14.8531 | 5.1441 |
| msgspec | 2.8771 | 12.8378 | 4.5797 |
| cysimdjson | 2.9870 | 9.5043 | 4.1598 |
| rapidjson | 4.7399 | 16.4090 | 6.7940 |
| ujson | 4.8417 | 18.3800 | 7.5532 |
| json | 4.9740 | 13.3385 | 6.3111 |

### Complete load of data/twitter.json

Sample file is 567916 bytes.

![](histograms/-Complete_load_of_data_twitter.json.svg 'Histogram for Complete load of data/twitter.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| orjson | 0.8338 | 10.9986 | 1.0194 |
| yyjson | 0.9109 | 14.9827 | 1.1691 |
| simdjson | 0.9728 | 12.3208 | 1.2150 |
| msgspec | 1.0663 | 10.1131 | 1.2464 |
| cysimdjson | 1.3475 | 8.0037 | 1.4957 |
| rapidjson | 2.0265 | 12.8124 | 2.2311 |
| json | 2.1085 | 10.1971 | 2.2773 |
| ujson | 2.1985 | 15.9313 | 2.4921 |

### Complete load of data/verysmall.json

Sample file is 7 bytes.

![](histograms/-Complete_load_of_data_verysmall.json.svg 'Histogram for Complete load of data/verysmall.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| msgspec | 0.0001 | 0.0004 | 0.0001 |
| orjson | 0.0001 | 0.0004 | 0.0001 |
| simdjson | 0.0002 | 0.0015 | 0.0002 |
| ujson | 0.0003 | 0.0023 | 0.0003 |
| yyjson | 0.0003 | 0.0012 | 0.0003 |
| rapidjson | 0.0003 | 0.0018 | 0.0003 |
| cysimdjson | 0.0003 | 0.0079 | 0.0003 |
| json | 0.0008 | 0.0103 | 0.0009 |

### Merge Patch

![](histograms/-Merge_Patch.svg 'Histogram for Merge Patch.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 0.0004 | 0.0014 | 0.0004 |
| json_merge_patch | 0.0005 | 0.0033 | 0.0005 |

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

