#!/usr/bin/env python3
from .cli import parse_args
from gendiff.generate_diff import generate_diff
from gendiff.formatters.format import format_diff


def main():
    args = parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    return print(format_diff(diff, args.format))


if __name__ == '__main__':
    main()
