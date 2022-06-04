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
| 188 | 🎉 expected result |
| 0 | 🔥 parsing should have failed but succeeded |
| 95 | 🔥 parsing should have succeeded but failed |
| 0 | ➕ result undefined, parsing succeeded |
| 35 | ➖ result undefined, parsing failed |


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
| cysimdjson | 5.9546 | 19.6696 | 10.0383 |
| msgspec | 5.9685 | 13.6818 | 9.4638 |
| simdjson | 6.4427 | 16.3638 | 11.1386 |
| orjson | 8.8252 | 16.7841 | 12.9363 |
| ujson | 9.9651 | 20.9605 | 15.2025 |
| json | 23.2570 | 30.3407 | 26.6418 |
| rapidjson | 24.2579 | 34.2014 | 29.2245 |

### Complete load of data/citm_catalog.json

Sample file is 1727030 bytes.

![](histograms/-Complete_load_of_data_citm_catalog.json.svg 'Histogram for Complete load of data/citm_catalog.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| simdjson | 3.2135 | 13.9585 | 5.2286 |
| cysimdjson | 3.3827 | 14.9411 | 4.9769 |
| orjson | 3.3990 | 10.9832 | 4.7538 |
| msgspec | 3.6584 | 11.8673 | 5.1431 |
| rapidjson | 4.9115 | 22.2681 | 6.7224 |
| ujson | 4.9775 | 15.4578 | 7.2002 |
| json | 5.3825 | 12.9017 | 6.5444 |

### Complete load of data/twitter.json

Sample file is 567916 bytes.

![](histograms/-Complete_load_of_data_twitter.json.svg 'Histogram for Complete load of data/twitter.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| orjson | 1.3505 | 7.6621 | 1.5121 |
| cysimdjson | 1.4218 | 7.0228 | 1.6907 |
| simdjson | 1.4306 | 11.1500 | 1.6655 |
| msgspec | 1.6621 | 8.3627 | 1.8380 |
| rapidjson | 2.1523 | 10.7129 | 2.3530 |
| ujson | 2.2734 | 12.6683 | 2.5384 |
| json | 2.2749 | 7.9442 | 2.4402 |

### Complete load of data/verysmall.json

Sample file is 7 bytes.

![](histograms/-Complete_load_of_data_verysmall.json.svg 'Histogram for Complete load of data/verysmall.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| msgspec | 0.0001 | 0.0005 | 0.0001 |
| orjson | 0.0001 | 0.0003 | 0.0002 |
| ujson | 0.0002 | 0.0042 | 0.0002 |
| rapidjson | 0.0003 | 0.0007 | 0.0003 |
| cysimdjson | 0.0004 | 0.0010 | 0.0004 |
| simdjson | 0.0005 | 0.0185 | 0.0005 |
| json | 0.0010 | 0.1977 | 0.0011 |

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

