#!/usr/bin/env python3
from .cli import parse_args
from gendiff.generate_diff import generate_diff


def main():
    args = parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    return print(diff)


if __name__ == '__main__':
    main()
