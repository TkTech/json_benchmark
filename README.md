# json_benchmark

This repository contains benchmarks for **Python** JSON readers & writers.
What's the fastest Python JSON parser? Let's find out.

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

<!-- end_correct_block -->


## Performance

<!-- start_performance_block -->


### Complete load of data/canada.json

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 5.5502 | 11.1734 | 7.8658 |
| cysimdjson | 5.7406 | 10.1619 | 7.9000 |
| simdjson | 5.7926 | 11.0426 | 8.2046 |
| orjson | 8.6017 | 15.0741 | 10.9376 |
| ujson | 10.0394 | 18.2333 | 12.9458 |
| json | 23.0770 | 28.5290 | 25.6070 |
| rapidjson | 25.7855 | 30.5490 | 28.3270 |


### Complete load of data/citm_catalog.json

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 3.0866 | 7.6158 | 3.9602 |
| simdjson | 3.0916 | 7.2800 | 3.9532 |
| cysimdjson | 3.2248 | 8.3841 | 4.5691 |
| orjson | 3.3885 | 7.4435 | 4.1514 |
| ujson | 4.9711 | 9.5521 | 5.9318 |
| rapidjson | 4.9867 | 9.2611 | 5.7957 |
| json | 5.2141 | 10.6472 | 6.0939 |


### Complete load of data/twitter.json

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| orjson | 1.2834 | 4.9193 | 1.3892 |
| cysimdjson | 1.3942 | 5.7907 | 1.6209 |
| simdjson | 1.4023 | 6.3474 | 1.5426 |
| yyjson | 1.4180 | 5.7103 | 1.5323 |
| rapidjson | 2.1790 | 6.4160 | 2.3069 |
| ujson | 2.1874 | 6.5209 | 2.3623 |
| json | 2.2601 | 6.0987 | 2.3854 |


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

