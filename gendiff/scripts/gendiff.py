#!/usr/bin/env python3
import argparse
from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--format", choices=['stylish', 'plain', 'json'],
        default='stylish', help="set format of output"
    )
    args = parser.parse_args()
    file1 = args.first_file
    file2 = args.second_file
    formatter = args.format
    return generate_diff(file1, file2, formatter)


if __name__ == '__main__':
    main()
