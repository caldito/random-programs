#!/usr/bin/env python3 

# Implement a find(1)-like tool, which looks for the path of regular files with a given name and prints them to stdout (find . -name SEARCH_NAME -type equivalent).

import argparse
import sys
from os import listdir
from os.path import abspath, isdir, isfile, join


def parse_args():
    parser = argparse.ArgumentParser(description='Optional app description')

    parser.add_argument('path',
                    help='follow new entries')
    parser.add_argument('-name',
                    required = False,
                    default="",
                    type=str,
                    help='')
    parser.add_argument('-type',
                    required = False,
                    default = "any",
                    type=str,
                    help='follow new entries')

    args = parser.parse_args()
    return args.path, args.name, args.type

def find(path, name, ftype):
    try:
        files = listdir(path)
        for f in files:
            file_path = join(path, f)
            print(file_path)
            if isdir(file_path):
                find(file_path, name, ftype)
    except NotADirectoryError:
        print("Error: The input should be a directory")
        sys.exit(1)
    except PermissionError:
        print("Not enough permissions to open " + path)
    except KeyboardInterrupt:
        sys.exit()

def main():
    path, name, ftype = parse_args()
    find(path, name, ftype)

if __name__ == "__main__":
    main()

