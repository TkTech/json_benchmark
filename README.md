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

| count | result |
| ----- | ------ |
| 283 | 🎉 expected result |
| 0 | 🔥 parsing should have failed but succeeded |
| 0 | 🔥 parsing should have succeeded but failed |
| 6 | ➕ result undefined, parsing succeeded |
| 29 | ➖ result undefined, parsing failed |


### rapidjson

| count | result |
| ----- | ------ |
| 277 | 🎉 expected result |
| 6 | 🔥 parsing should have failed but succeeded |
| 0 | 🔥 parsing should have succeeded but failed |
| 6 | ➕ result undefined, parsing succeeded |
| 29 | ➖ result undefined, parsing failed |


### orjson

| count | result |
| ----- | ------ |
| 283 | 🎉 expected result |
| 0 | 🔥 parsing should have failed but succeeded |
| 0 | 🔥 parsing should have succeeded but failed |
| 5 | ➕ result undefined, parsing succeeded |
| 30 | ➖ result undefined, parsing failed |


### simdjson

| count | result |
| ----- | ------ |
| 283 | 🎉 expected result |
| 0 | 🔥 parsing should have failed but succeeded |
| 0 | 🔥 parsing should have succeeded but failed |
| 8 | ➕ result undefined, parsing succeeded |
| 27 | ➖ result undefined, parsing failed |


### ujson

| count | result |
| ----- | ------ |
| 257 | 🎉 expected result |
| 26 | 🔥 parsing should have failed but succeeded |
| 0 | 🔥 parsing should have succeeded but failed |
| 16 | ➕ result undefined, parsing succeeded |
| 19 | ➖ result undefined, parsing failed |


### msgspec

| count | result |
| ----- | ------ |
| 283 | 🎉 expected result |
| 0 | 🔥 parsing should have failed but succeeded |
| 0 | 🔥 parsing should have succeeded but failed |
| 6 | ➕ result undefined, parsing succeeded |
| 29 | ➖ result undefined, parsing failed |


<!-- end_correct_block -->


## Performance

<!-- start_performance_block -->


### Complete load of data/canada.json

Sample file is 2251051 bytes.

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 5.4603 | 13.5752 | 9.9340 |
| msgspec | 5.7863 | 12.7752 | 8.8813 |
| cysimdjson | 5.8038 | 10.5372 | 8.0821 |
| simdjson | 5.8468 | 14.2203 | 10.0390 |
| orjson | 8.5500 | 15.9159 | 11.9144 |
| ujson | 9.8216 | 20.6018 | 14.2988 |
| json | 23.6868 | 30.5128 | 26.8572 |
| rapidjson | 25.6958 | 33.4925 | 29.4259 |

### Complete load of data/citm_catalog.json

Sample file is 1727030 bytes.

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| simdjson | 3.0281 | 10.9173 | 4.7469 |
| yyjson | 3.1265 | 11.0829 | 4.8833 |
| cysimdjson | 3.3061 | 8.4879 | 4.4922 |
| orjson | 3.3289 | 11.3524 | 4.6075 |
| msgspec | 3.6390 | 12.0191 | 4.9355 |
| ujson | 4.9217 | 15.6031 | 6.7237 |
| rapidjson | 4.9250 | 11.9337 | 6.2165 |
| json | 5.3019 | 12.8375 | 6.3753 |

### Complete load of data/twitter.json

Sample file is 567916 bytes.

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| orjson | 1.3158 | 7.3897 | 1.4485 |
| simdjson | 1.3640 | 9.9401 | 1.5521 |
| cysimdjson | 1.3851 | 5.8494 | 1.5904 |
| yyjson | 1.3990 | 8.8561 | 1.5849 |
| msgspec | 1.6705 | 7.6091 | 1.8395 |
| rapidjson | 2.1353 | 8.1012 | 2.2955 |
| ujson | 2.2779 | 10.3709 | 2.4661 |
| json | 2.2999 | 8.1822 | 2.4501 |

### Complete load of data/verysmall.json

Sample file is 7 bytes.

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| msgspec | 0.0001 | 0.0002 | 0.0001 |
| orjson | 0.0002 | 0.0031 | 0.0002 |
| ujson | 0.0002 | 0.0003 | 0.0002 |
| yyjson | 0.0002 | 0.0171 | 0.0002 |
| rapidjson | 0.0003 | 0.0007 | 0.0003 |
| cysimdjson | 0.0003 | 0.0014 | 0.0004 |
| simdjson | 0.0004 | 0.0011 | 0.0005 |
| json | 0.0010 | 0.0080 | 0.0011 |

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

