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

Sample file is 2251051 bytes.

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 5.2855 | 14.6124 | 9.5136 |
| simdjson | 5.7374 | 14.3674 | 9.5140 |
| cysimdjson | 5.9193 | 10.7559 | 8.2352 |
| orjson | 8.4625 | 18.6653 | 11.8414 |
| ujson | 10.1251 | 18.8607 | 14.3548 |
| json | 23.1732 | 30.2110 | 26.2201 |
| rapidjson | 25.4896 | 34.1050 | 29.1916 |


### Complete load of data/citm_catalog.json

Sample file is 1727030 bytes.

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| simdjson | 3.0496 | 10.2288 | 4.5276 |
| yyjson | 3.0725 | 12.9260 | 4.7278 |
| cysimdjson | 3.2350 | 9.2566 | 4.6005 |
| orjson | 3.2869 | 8.9607 | 4.3607 |
| rapidjson | 4.8654 | 10.7684 | 6.0624 |
| ujson | 4.9233 | 12.8696 | 6.5945 |
| json | 5.2351 | 9.3376 | 6.1055 |


### Complete load of data/twitter.json

Sample file is 567916 bytes.

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| orjson | 1.3714 | 6.0291 | 1.4893 |
| yyjson | 1.3791 | 9.2868 | 1.5647 |
| simdjson | 1.3860 | 8.8234 | 1.5560 |
| cysimdjson | 1.3954 | 6.9549 | 1.6465 |
| rapidjson | 2.1363 | 8.4668 | 2.2876 |
| ujson | 2.2646 | 9.1984 | 2.4557 |
| json | 2.2850 | 6.2415 | 2.3875 |


### Complete load of data/verysmall.json

Sample file is 7 bytes.

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| orjson | 0.0002 | 0.0028 | 0.0002 |
| ujson | 0.0002 | 0.0003 | 0.0002 |
| yyjson | 0.0002 | 0.0007 | 0.0002 |
| rapidjson | 0.0003 | 0.0009 | 0.0003 |
| cysimdjson | 0.0004 | 0.0010 | 0.0004 |
| simdjson | 0.0004 | 0.0011 | 0.0005 |
| json | 0.0010 | 0.0115 | 0.0011 |


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

