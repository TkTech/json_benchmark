# json_benchmark

<!-- start_last_updated_block -->


> :grey_exclamation: Benchmarks regenerated on 2022-08-07

<!-- end_last_updated_block -->


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
| orjson     | Yes    | Yes    | 3.7.11  |
| rapidjson  | Yes    | Yes    | 1.6     |
| ujson      | Yes    | Yes    | 5.2.0   |
| json       | Yes    | Yes    | 3.10    |
| msgspec    | Yes    | Yes    | 0.7.0   |

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
| 6 | ➕ result undefined, parsing succeeded |
| 29 | ➖ result undefined, parsing failed |

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
| cysimdjson | 5.6900 | 11.0865 | 8.2301 |
| simdjson | 5.9691 | 18.1188 | 12.9032 |
| msgspec | 6.2665 | 14.6609 | 9.8614 |
| orjson | 7.4561 | 17.3678 | 11.7010 |
| yyjson | 7.9872 | 19.1369 | 13.8361 |
| ujson | 9.9928 | 20.4961 | 15.0385 |
| json | 23.1498 | 35.7078 | 31.5420 |
| rapidjson | 23.7818 | 34.4833 | 28.8178 |


### Complete load of data/citm_catalog.json

Sample file is 1727204 bytes.

![](histograms/-Complete_load_of_data_citm_catalog.json.svg 'Histogram for Complete load of data/citm_catalog.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| msgspec | 3.0556 | 11.2726 | 4.4346 |
| simdjson | 3.1650 | 15.4434 | 5.5860 |
| cysimdjson | 3.3487 | 9.5261 | 4.6820 |
| orjson | 3.5784 | 13.4451 | 5.3176 |
| yyjson | 4.2500 | 16.7959 | 6.7714 |
| rapidjson | 5.0066 | 13.0181 | 6.6638 |
| ujson | 5.0782 | 15.5697 | 7.2611 |
| json | 5.9400 | 12.4006 | 7.2006 |


### Complete load of data/twitter.json

Sample file is 631514 bytes.

![](histograms/-Complete_load_of_data_twitter.json.svg 'Histogram for Complete load of data/twitter.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| msgspec | 1.0906 | 8.0987 | 1.2462 |
| orjson | 1.1547 | 8.5405 | 1.3243 |
| cysimdjson | 1.4119 | 6.1546 | 1.6388 |
| simdjson | 1.4126 | 11.2883 | 1.6574 |
| yyjson | 1.6139 | 12.2784 | 1.8747 |
| rapidjson | 2.1710 | 10.8341 | 2.5329 |
| json | 2.2981 | 8.2583 | 2.4406 |
| ujson | 2.4385 | 12.0872 | 2.7202 |


### Complete load of data/verysmall.json

Sample file is 7 bytes.

![](histograms/-Complete_load_of_data_verysmall.json.svg 'Histogram for Complete load of data/verysmall.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| msgspec | 0.0001 | 0.0003 | 0.0001 |
| orjson | 0.0001 | 0.0257 | 0.0002 |
| yyjson | 0.0002 | 0.0251 | 0.0004 |
| ujson | 0.0003 | 0.0009 | 0.0003 |
| cysimdjson | 0.0003 | 0.0081 | 0.0004 |
| simdjson | 0.0004 | 0.0015 | 0.0005 |
| rapidjson | 0.0004 | 0.0011 | 0.0005 |
| json | 0.0010 | 0.0062 | 0.0010 |


### Merge Patch

![](histograms/-Merge_Patch.svg 'Histogram for Merge Patch.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 0.0003 | 0.0015 | 0.0003 |
| json_merge_patch | 0.0005 | 0.0080 | 0.0005 |


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

