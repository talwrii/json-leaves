import argparse
import json
import sys
from types import NoneType


def get_nodes(tree, prefix=()):
    yield tree_type(tree), prefix, tree
    if isinstance(tree, dict):
        for k, v in tree.items():
            yield from get_nodes(v, prefix + (k,))
    elif isinstance(tree, list):
        yield NODE, prefix, tree
        for i, v in enumerate(tree):
            yield from get_nodes(v, prefix + (i,))
    elif isinstance(tree, (NoneType, float, int, str)):
        pass
    else:
        raise ValueError(tree)


PARSER = argparse.ArgumentParser(description='Extract the leaves from a JSON file and show the paths to said leaves')
PARSER.add_argument('--quote', "-q", action='store_true', help="Quote output")
pathmx = PARSER.add_mutually_exclusive_group()
patmx = pathmx.add_argument('--jq', "-J", action='store_true', help="Output paths for js")
patmx = pathmx.add_argument('--python', "--py", "-c", "--java", action='store_true', help="Output paths for python / C / Java")
fmtmx = PARSER.add_mutually_exclusive_group()
fmtmx.add_argument('--json', "-j", action='store_true', help="Use JSON format")
fmtmx.add_argument('--jsonl', "-l", action='store_true', help="Use JSONL line format")
nodemx = PARSER.add_mutually_exclusive_group()
nodemx.add_argument('--nodes', "-n", action='store_true', default=False, help="Show nodes as well as leaves")
nodemx.add_argument('--values', "-v", action='store_true', default=False, help="Only show values")
nodemx.add_argument('--paths', "-p", action='store_true', default=False, help="Only show values")


args = PARSER.parse_args()



NODE = 'node'
LEAF = 'leaf'

def tree_type(x):
    if isinstance(x, (int, float, str, NoneType)):
        return LEAF
    else:
        return NODE

def jq_fmt_path(path):
    if not path:
        return "."

    result = []
    for p in path:
        if isinstance(p, int):
            result.append(f'[{p}]')
        elif isinstance(p, str):
            result.append(f'.{p}')
    return ''.join(result)

def python_fmt_path(path):
    if not path:
        return ""

    result = []
    for p in path:
        if isinstance(p, int):
            result.append(f'[{p}]')
        elif isinstance(p, str):
            result.append(f'["{p}"]')
    return ''.join(result)

def main():
    data = get_nodes(json.loads(sys.stdin.read()))
    if not args.nodes:
        data = [(t, p, v) for (t, p, v) in data if t == LEAF]

    if args.jq:
        fmt_path = jq_fmt_path
    elif args.python:
        fmt_path = python_fmt_path
    else:
        fmt_path = jq_fmt_path

    if args.quote:
        fmt_value = json.dumps
    else:
        fmt_value = str

    if args.jsonl:
        for _, path, value in data:
            print(json.dumps([fmt_path(path), value]))
    elif args.json:
        print(json.dumps([[fmt_path(path), value] for _, path, value in data]))
    else:
        for node_type, path, value in data:
            if args.values:
                print(fmt_value(value))
                continue

            if args.paths:
                print(fmt_path(path))



            match node_type:
                case "node":
                    if args.python and not path:
                        # ignore this problem
                        pass
                    print(fmt_path(path), json.dumps(value))
                case "leaf":
                    print(fmt_path(path), fmt_value(value))
