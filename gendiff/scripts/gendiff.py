#!/usr/bin/env python3
import argparse
from gendiff import parse_files
from gendiff import generate_diff
from gendiff.formatters.stylish import format_stylish


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    file1 = parse_files(args.first_file)
    file2 = parse_files(args.second_file)
    return format_stylish(generate_diff(file1, file2))


if __name__ == '__main__':
    main()
