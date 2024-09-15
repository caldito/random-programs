#!/usr/bin/env python3 

# Implement a tail(1)-like tool, which prints last N lines for a file provided as a param and watch for the new entries and print them on stdout until interrupted (tail -f -n N equivalent).

import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='Optional app description')

    parser.add_argument('path',
                    help='follow new entries')
    parser.add_argument('-n',
                    required = False,
                    default=10,
                    type=int,
                    help='follow new entries')
    parser.add_argument('-f', '--follow',
                    required = False,
                    action='store_true',
                    help='follow new entries')

    args = parser.parse_args()
    return args.path, args.follow, args.n

def tail(path, follow, lines):
    try:
        fd = open(path)
    except OSError:
        print ("Could not open/read file: " + path)
        sys.exit()

    last_lines = []

    while True:
        if len(last_lines) > lines:
            last_lines.pop(0)
        line = fd.readline()
        if not line:
            break
        last_lines.append(line)
 
    for line in last_lines:
        print(line, end='')
    
    if follow:
        while True:
            try:
                new_content = fd.read()
                print(new_content, end='')
            except KeyboardInterrupt:
                fd.close()
                sys.exit()
    else:
        fd.close()

def main():
    path, follow, lines = parse_args()
    tail(path, follow, lines)

if __name__ == "__main__":
    main()

