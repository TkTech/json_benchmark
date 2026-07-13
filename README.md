# json_benchmark

<!-- start_last_updated_block -->


> :grey_exclamation: Benchmarks regenerated on 2026-07-13

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
| yyjson | 8.6970 | 9.3007 | 8.8893 |
| ijson (yajl2_c) | 22.6858 | 23.8652 | 23.1013 |


### Streaming parse of data/citm_catalog.json

Sample file is 1727204 bytes.

![](histograms/-Streaming_parse_of_data_citm_catalog.json.svg 'Histogram for Streaming parse of data/citm_catalog.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 3.3277 | 4.8824 | 3.7323 |
| ijson (yajl2_c) | 6.3018 | 8.5975 | 6.9487 |


### Streaming parse of data/twitter.json

Sample file is 631514 bytes.

![](histograms/-Streaming_parse_of_data_twitter.json.svg 'Histogram for Streaming parse of data/twitter.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 1.7940 | 2.0859 | 1.8278 |
| ijson (yajl2_c) | 2.8267 | 5.3436 | 2.9626 |


### Streaming parse of data/verysmall.json

Sample file is 7 bytes.

![](histograms/-Streaming_parse_of_data_verysmall.json.svg 'Histogram for Streaming parse of data/verysmall.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 0.0011 | 0.0212 | 0.0012 |
| ijson (yajl2_c) | 0.0037 | 0.1267 | 0.0039 |


### Streaming parse of data/fgo.json

Sample file is 48765043 bytes.

![](histograms/-Streaming_parse_of_data_fgo.json.svg 'Histogram for Streaming parse of data/fgo.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 315.4146 | 319.3040 | 317.5809 |
| ijson (yajl2_c) | 495.1035 | 505.1622 | 499.9637 |


### Streaming parse of data/otfcc.json

Sample file is 66409302 bytes.

![](histograms/-Streaming_parse_of_data_otfcc.json.svg 'Histogram for Streaming parse of data/otfcc.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 646.0111 | 659.2554 | 651.9847 |
| ijson (yajl2_c) | 1020.1002 | 1032.1442 | 1027.0863 |


### Streaming parse of data/poet.json

Sample file is 3512883 bytes.

![](histograms/-Streaming_parse_of_data_poet.json.svg 'Histogram for Streaming parse of data/poet.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 7.6482 | 11.5492 | 7.8543 |
| ijson (yajl2_c) | 9.3670 | 9.6594 | 9.5128 |


### Streaming parse of data/gsoc-2018.json

Sample file is 3327831 bytes.

![](histograms/-Streaming_parse_of_data_gsoc-2018.json.svg 'Histogram for Streaming parse of data/gsoc-2018.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 4.7380 | 5.4931 | 4.8932 |
| ijson (yajl2_c) | 5.1025 | 5.9048 | 5.2717 |


### Complete load of data/canada.json

Sample file is 2251051 bytes.

![](histograms/-Complete_load_of_data_canada.json.svg 'Histogram for Complete load of data/canada.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 4.4991 | 6.7486 | 4.8984 |
| orjson | 6.0146 | 20.8946 | 12.1758 |
| msgspec | 6.6082 | 27.9779 | 15.5113 |
| simdjson | 7.2701 | 20.6712 | 14.5211 |
| ujson | 11.1293 | 25.2489 | 18.3757 |
| json | 23.8417 | 34.6569 | 28.9730 |
| rapidjson | 24.6718 | 39.5648 | 32.8370 |


### Complete load of data/citm_catalog.json

Sample file is 1727030 bytes.

![](histograms/-Complete_load_of_data_citm_catalog.json.svg 'Histogram for Complete load of data/citm_catalog.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 1.7838 | 3.2357 | 1.9707 |
| orjson | 2.4194 | 13.5199 | 4.6141 |
| msgspec | 3.0889 | 21.4627 | 6.3947 |
| simdjson | 3.3927 | 16.4161 | 6.1467 |
| ujson | 4.4742 | 19.0578 | 7.3929 |
| rapidjson | 4.5165 | 21.7992 | 7.4734 |
| json | 6.2320 | 14.9818 | 7.9924 |


### Complete load of data/twitter.json

Sample file is 567916 bytes.

![](histograms/-Complete_load_of_data_twitter.json.svg 'Histogram for Complete load of data/twitter.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| orjson | 0.8095 | 13.5349 | 1.1043 |
| yyjson | 0.8694 | 1.5064 | 0.9441 |
| msgspec | 1.0577 | 17.2088 | 1.4776 |
| simdjson | 1.3933 | 14.9575 | 1.7529 |
| ujson | 1.6982 | 14.8908 | 2.1086 |
| rapidjson | 1.8627 | 15.8346 | 2.2719 |
| json | 2.6851 | 13.7934 | 2.9656 |


### Complete load of data/verysmall.json

Sample file is 7 bytes.

![](histograms/-Complete_load_of_data_verysmall.json.svg 'Histogram for Complete load of data/verysmall.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| msgspec | 0.0001 | 0.0039 | 0.0001 |
| yyjson | 0.0001 | 0.0025 | 0.0001 |
| orjson | 0.0001 | 0.0017 | 0.0001 |
| rapidjson | 0.0003 | 0.0017 | 0.0003 |
| ujson | 0.0003 | 0.0043 | 0.0003 |
| simdjson | 0.0004 | 0.0098 | 0.0004 |
| json | 0.0008 | 0.0049 | 0.0008 |


### Complete load of data/fgo.json

Sample file is 45690911 bytes.

![](histograms/-Complete_load_of_data_fgo.json.svg 'Histogram for Complete load of data/fgo.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 226.2088 | 239.0445 | 230.9776 |
| orjson | 470.7608 | 544.2078 | 507.9765 |
| msgspec | 474.9090 | 539.3030 | 508.0502 |
| rapidjson | 607.6599 | 671.6313 | 642.6487 |
| json | 658.0721 | 700.5949 | 674.1365 |
| ujson | 795.8875 | 926.3975 | 873.1998 |
| simdjson | 852.5420 | 919.4318 | 881.5412 |


### Complete load of data/otfcc.json

Sample file is 66409251 bytes.

![](histograms/-Complete_load_of_data_otfcc.json.svg 'Histogram for Complete load of data/otfcc.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| yyjson | 559.2589 | 575.5079 | 570.1669 |
| msgspec | 1051.5780 | 1180.5235 | 1115.4705 |
| orjson | 1105.1228 | 1175.1532 | 1142.0121 |
| ujson | 1286.0061 | 1469.6067 | 1364.5810 |
| rapidjson | 1296.9691 | 1427.1810 | 1359.3918 |
| simdjson | 1357.0520 | 1529.2694 | 1430.5631 |
| json | 1572.2035 | 1680.6050 | 1615.5561 |


### Complete load of data/poet.json

Sample file is 1707203 bytes.

![](histograms/-Complete_load_of_data_poet.json.svg 'Histogram for Complete load of data/poet.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| orjson | 4.4288 | 5.2035 | 4.5914 |
| yyjson | 4.6131 | 5.3194 | 4.7907 |
| msgspec | 4.7112 | 6.7624 | 5.3332 |
| simdjson | 5.2242 | 6.5857 | 5.4582 |
| ujson | 5.7027 | 8.0437 | 6.4811 |
| json | 6.3685 | 9.7802 | 7.2586 |
| rapidjson | 7.4218 | 8.2376 | 7.6006 |


### Complete load of data/gsoc-2018.json

Sample file is 3327831 bytes.

![](histograms/-Complete_load_of_data_gsoc-2018.json.svg 'Histogram for Complete load of data/gsoc-2018.json.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| msgspec | 2.5023 | 14.6973 | 3.0122 |
| yyjson | 2.5452 | 3.1216 | 2.6679 |
| simdjson | 2.8363 | 17.3013 | 3.2583 |
| orjson | 3.5744 | 14.2182 | 3.7913 |
| rapidjson | 4.3007 | 17.6994 | 4.7676 |
| json | 4.4708 | 16.9558 | 5.2436 |
| ujson | 4.6627 | 22.6703 | 5.6661 |


### Merge Patch

![](histograms/-Merge_Patch.svg 'Histogram for Merge Patch.')

| library | min (ms) | max (ms) | mean (ms) |
| ------- | -------- | -------- | --------- |
| json_merge_patch | 0.0005 | 0.0803 | 0.0007 |
| yyjson | 0.0010 | 0.0277 | 0.0011 |


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

