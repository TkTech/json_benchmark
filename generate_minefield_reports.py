"""
Small utility script to check each library for compliance with the JSON
minefield (https://github.com/nst/JSONTestSuite)

When run, it will also update the summaries in the README.md.
"""
import sys
from datetime import datetime
from pathlib import Path

from humanmark import Fragment, Text, Header, Paragraph, dump, load, HTMLBlock, \
    Link


def do_yyjson(content):
    import yyjson
    yyjson.Document(content)


def do_rapidjson(content):
    import rapidjson
    rapidjson.loads(content)


def do_orjson(content):
    import orjson
    orjson.loads(content)


def do_ujson(content):
    import ujson
    ujson.loads(content)


def do_simdjson(content):
    import simdjson
    p = simdjson.Parser()
    p.parse(content)


def do_msgspec(content):
    import msgspec
    msgspec.json.decode(content.encode('utf-8'))


def run_minefield(do_parse, tests):
    tally = {
        'expected_result': 0,
        'should_have_failed': 0,
        'should_have_passed': 0,
        'undefined_passed': 0,
        'undefined_failed': 0
    }

    results = []

    for expected_result, files in tests.items():
        for file in files:
            with open(file) as src:
                try:
                    do_parse(src.read())
                except Exception:  # noqa
                    key = {'y': 'should_have_passed',
                           'n': 'expected_result',
                           'i': 'undefined_failed'}[expected_result]
                else:
                    key = {'y': 'expected_result',
                           'n': 'should_have_failed',
                           'i': 'undefined_passed'}[expected_result]

                results.append((expected_result, file, key))
                tally[key] += 1

    return {
        'tally': tally,
        'results': results
    }


def label(k) -> str:
    return {'expected_result': '🎉 expected result',
            'should_have_passed': '🔥 parsing should have succeeded but failed',
            'should_have_failed': '🔥 parsing should have failed but succeeded',
            'undefined_passed': '➕ result undefined, parsing succeeded',
            'undefined_failed': '➖ result undefined, parsing failed'}[k]


def main(argv):
    # All tests categorized by the expected test status (pass, fail,
    # unspecified).
    tests = {
        'y': list((Path('data') / 'minefield').glob('y_*.json')),
        'n': list((Path('data') / 'minefield').glob('n_*.json')),
        'i': list((Path('data') / 'minefield').glob('i_*.json'))
    }

    runners = [
        ('yyjson', do_yyjson),
        ('rapidjson', do_rapidjson),
        ('orjson', do_orjson),
        ('simdjson', do_simdjson),
        ('ujson', do_ujson),
        ('msgspec', do_msgspec),
    ]

    readme_summary = Fragment()

    for library, runner in runners:
        results = run_minefield(runner, tests)

        # I never bothered adding table support to HumanMark...this
        # is good motivation to go do that...
        # We'll use this summary in the complete output as well as in the
        # root README.
        summary = Paragraph(children=[
            Text('| count | result |\n'),
            Text('| ----- | ------ |\n'),
            *(
                Text(f'| {v} | {label(k)} |\n')
                for k, v in results['tally'].items()
            )
        ])

        fragment = Fragment(children=[
            Header(1, children=[Text(f'Minefield results for {library}')]),
            Paragraph(children=[
                Text(f'Generated {datetime.now()}.')
            ]),
            Header(2, children=[Text('Summary')]),
            summary,
            Header(3, children=[Text('Complete Results')]),
            Paragraph(children=[
                Text('| file | result |\n'),
                Text('| ---- | ------ |\n'),
                *(
                    Text(f'| {file} | {label(key)} |\n')
                    for _, file, key in results['results']
                )
            ])
        ])

        with open(Path('minefield_reports') / f'{library}.md', 'w') as out:
            dump(fragment, out)

        readme_summary.extend((
            Header(3, children=[Text(library)]),
            Paragraph(children=[
                Text('See full minefield results for '),
                Link(
                    f'minefield_reports/{library}.md',
                    children=[
                        Text(library)
                    ]
                ),
                Text('.')
            ]),
            summary.unlink()
        ))

    with open('README.md') as src:
        readme = load(src)

        start = readme.find_one(
            HTMLBlock,
            f=lambda block: block.content == '<!-- start_correct_block -->\n'
        )

        end = readme.find_one(
            HTMLBlock,
            f=lambda block: block.content == '<!-- end_correct_block -->\n'
        )

        # Erase all the content between the open and closing blocks.
        node = start.next
        while node:
            if node == end:
                break

            node = node.delete()

        # Insert our summary blocks
        start.append_sibling(readme_summary)

    with open('README.md', 'w') as out:
        dump(readme, out)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
