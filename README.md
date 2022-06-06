# json_benchmark

This repository contains benchmarks for **Python** JSON readers & writers.
What's the fastest Python JSON parser? Let's find out.

To run the tests yourself:

```bash
git clone git@github.com:TkTech/json_benchmark.git && cd json_benchmark
<setup a virtualenv using your tool of choice>
pip install -r requirements.txt
pytest --benchmark-json benchmark.json
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
| 5 | ➕ result undefined, parsing succeeded |
| 30 | ➖ result undefined, parsing failed |


### simdjson

See full minefield results for [simdjson](minefield_reports/simdjson.md).

| count | result |
| ----- | ------ |
| 283 | 🎉 expected result |
| 0 | 🔥 parsing should have failed but succeeded |
| 0 | 🔥 parsing should have succeeded but failed |
| 8 | ➕ result undefined, parsing succeeded |
| 27 | ➖ result undefined, parsing failed |


### ujson

See full minefield results for [ujson](minefield_reports/ujson.md).

| count | result |
| ----- | ------ |
| 257 | 🎉 expected result |
| 26 | 🔥 parsing should have failed but succeeded |
| 0 | 🔥 parsing should have succeeded but failed |
| 16 | ➕ result undefined, parsing succeeded |
| 19 | ➖ result undefined, parsing failed |


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
| yyjson | 5.7710 | 29.4514 | 16.1943 |
| msgspec | 5.9699 | 25.9816 | 13.6442 |
| cysimdjson | 6.0465 | 22.5093 | 11.1078 |
| simdjson | 6.3914 | 38.4171 | 16.3602 |
| orjson | 8.7645 | 28.6002 | 17.5204 |
| ujson | 10.1288 | 36.4500 | 21.6160 |
| json | 23.7460 | 40.3626 | 29.9333 |
| rapidjson | 25.1285 | 44.9850 | 34.1460 |

### Complete load of data/citm_catalog.json

Sample file is 1727030 bytes.

![](histograms/-Complete_load_of_data_citm_catalog.json.svg 'Histogram for Complete load of data/citm_catalog.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 3.2003 | 31.8698 | 8.9378 |
| simdjson | 3.2444 | 27.3618 | 8.0252 |
| orjson | 3.4045 | 22.3979 | 6.6422 |
| cysimdjson | 3.5063 | 16.1367 | 5.8227 |
| msgspec | 3.6509 | 23.4007 | 6.9979 |
| ujson | 4.8042 | 28.5217 | 9.7305 |
| rapidjson | 4.9504 | 26.5347 | 8.7840 |
| json | 5.3869 | 25.1608 | 8.2204 |

### Complete load of data/twitter.json

Sample file is 567916 bytes.

![](histograms/-Complete_load_of_data_twitter.json.svg 'Histogram for Complete load of data/twitter.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| orjson | 1.3453 | 19.1929 | 1.6650 |
| simdjson | 1.4265 | 19.8124 | 1.8580 |
| yyjson | 1.4392 | 22.6408 | 1.8669 |
| cysimdjson | 1.5399 | 8.9231 | 1.7728 |
| msgspec | 1.6854 | 16.8773 | 2.0062 |
| rapidjson | 2.2008 | 19.0686 | 2.5841 |
| ujson | 2.2946 | 23.4167 | 2.8156 |
| json | 2.3422 | 16.9511 | 2.6148 |

### Complete load of data/verysmall.json

Sample file is 7 bytes.

![](histograms/-Complete_load_of_data_verysmall.json.svg 'Histogram for Complete load of data/verysmall.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| msgspec | 0.0001 | 0.0003 | 0.0001 |
| orjson | 0.0001 | 0.0003 | 0.0002 |
| yyjson | 0.0002 | 0.0014 | 0.0002 |
| ujson | 0.0002 | 0.0003 | 0.0002 |
| rapidjson | 0.0003 | 0.0012 | 0.0003 |
| cysimdjson | 0.0004 | 0.0012 | 0.0004 |
| simdjson | 0.0005 | 0.0035 | 0.0006 |
| json | 0.0011 | 0.0054 | 0.0012 |

### Merge Patch

![](histograms/-Merge_Patch.svg 'Histogram for Merge Patch.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 0.0003 | 0.0017 | 0.0003 |
| json_merge_patch | 0.0006 | 0.0085 | 0.0006 |

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

