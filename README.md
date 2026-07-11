# json_benchmark

<!-- start_last_updated_block -->


> :grey_exclamation: Benchmarks regenerated on 2026-07-11

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

| Library    | Reader | Writer | Streaming | Version |
|------------|--------|--------|-----------|---------|
| simdjson   | Yes    | No     | No        | 7.0.3   |
| cysimdjson | Yes    | No     | No        | 23.9    |
| yyjson     | Yes    | Yes    | Yes       | 5.0.0   |
| orjson     | Yes    | Yes    | No        | 3.11.9  |
| rapidjson  | Yes    | Yes    | No        | 1.23    |
| ujson      | Yes    | Yes    | No        | 5.13.0  |
| json       | Yes    | Yes    | No        | 3.11    |
| msgspec    | Yes    | Yes    | No        | 0.21.1  |
| ijson      | Yes    | No     | Yes       | 3.5.1   |

"Streaming" indicates a SAX-style / incremental parser that dispatches JSON
tokens without building the whole document in memory. These are compared
separately in the "Streaming parse of ..." benchmark groups.

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


### yyjson-sax

See full minefield results for [yyjson-sax](minefield_reports/yyjson-sax.md).

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
| 4 | ➕ result undefined, parsing succeeded |
| 31 | ➖ result undefined, parsing failed |


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


### ijson

See full minefield results for [ijson](minefield_reports/ijson.md).

| count | result |
| ----- | ------ |
| 282 | 🎉 expected result |
| 1 | 🔥 parsing should have failed but succeeded |
| 0 | 🔥 parsing should have succeeded but failed |
| 16 | ➕ result undefined, parsing succeeded |
| 19 | ➖ result undefined, parsing failed |


<!-- end_correct_block -->


## Performance

In these benchmarks, lower is better.

<!-- start_performance_block -->


### Streaming parse of data/canada.json

Sample file is 2251051 bytes.

![](histograms/-Streaming_parse_of_data_canada.json.svg 'Histogram for Streaming parse of data/canada.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 8.8950 | 13.4254 | 9.5058 |
| ijson (yajl2_c) | 24.3511 | 28.3819 | 25.3745 |

### Streaming parse of data/citm_catalog.json

Sample file is 1727204 bytes.

![](histograms/-Streaming_parse_of_data_citm_catalog.json.svg 'Histogram for Streaming parse of data/citm_catalog.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 3.7303 | 5.7675 | 4.0534 |
| ijson (yajl2_c) | 7.0771 | 10.9903 | 7.8962 |

### Streaming parse of data/twitter.json

Sample file is 631514 bytes.

![](histograms/-Streaming_parse_of_data_twitter.json.svg 'Histogram for Streaming parse of data/twitter.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 1.9840 | 2.6766 | 2.0886 |
| ijson (yajl2_c) | 3.1829 | 5.3100 | 3.3930 |

### Streaming parse of data/verysmall.json

Sample file is 7 bytes.

![](histograms/-Streaming_parse_of_data_verysmall.json.svg 'Histogram for Streaming parse of data/verysmall.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 0.0010 | 0.1257 | 0.0011 |
| ijson (yajl2_c) | 0.0037 | 0.0286 | 0.0041 |

### Complete load of data/canada.json

Sample file is 2251051 bytes.

![](histograms/-Complete_load_of_data_canada.json.svg 'Histogram for Complete load of data/canada.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| orjson | 5.6353 | 20.3192 | 12.0326 |
| yyjson | 6.0868 | 24.8159 | 13.6109 |
| msgspec | 6.2057 | 18.5555 | 11.4317 |
| simdjson | 6.7152 | 22.1631 | 13.2035 |
| ujson | 10.6807 | 27.6078 | 18.3567 |
| json | 23.4137 | 35.6167 | 28.4750 |
| rapidjson | 23.4955 | 35.5762 | 29.5386 |

### Complete load of data/citm_catalog.json

Sample file is 1727030 bytes.

![](histograms/-Complete_load_of_data_citm_catalog.json.svg 'Histogram for Complete load of data/citm_catalog.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| orjson | 2.2924 | 17.2998 | 4.7394 |
| msgspec | 2.9279 | 16.1749 | 4.7772 |
| yyjson | 3.0563 | 20.5972 | 6.2553 |
| simdjson | 3.2246 | 19.1667 | 5.8622 |
| ujson | 4.2557 | 26.9695 | 7.4381 |
| rapidjson | 4.3142 | 20.1385 | 6.9346 |
| json | 6.1490 | 14.7257 | 7.6981 |

### Complete load of data/twitter.json

Sample file is 567916 bytes.

![](histograms/-Complete_load_of_data_twitter.json.svg 'Histogram for Complete load of data/twitter.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| orjson | 0.7891 | 13.3578 | 1.0326 |
| msgspec | 1.0239 | 12.2415 | 1.2897 |
| yyjson | 1.2202 | 18.0516 | 1.6326 |
| simdjson | 1.3748 | 15.9009 | 1.6798 |
| ujson | 1.6601 | 14.2774 | 2.0449 |
| rapidjson | 1.8364 | 13.6781 | 2.0960 |
| json | 2.6590 | 10.6174 | 2.8569 |

### Complete load of data/verysmall.json

Sample file is 7 bytes.

![](histograms/-Complete_load_of_data_verysmall.json.svg 'Histogram for Complete load of data/verysmall.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| msgspec | 0.0001 | 0.0013 | 0.0001 |
| orjson | 0.0001 | 0.0004 | 0.0001 |
| yyjson | 0.0002 | 0.0059 | 0.0003 |
| rapidjson | 0.0003 | 0.0015 | 0.0003 |
| ujson | 0.0003 | 0.0028 | 0.0003 |
| simdjson | 0.0004 | 0.0026 | 0.0004 |
| json | 0.0008 | 0.0412 | 0.0009 |

### Merge Patch

![](histograms/-Merge_Patch.svg 'Histogram for Merge Patch.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| json_merge_patch | 0.0004 | 0.0224 | 0.0005 |
| yyjson | 0.0008 | 0.0272 | 0.0009 |

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

