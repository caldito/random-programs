#!/usr/bin/env python3 

# Implement a tail(1)-like tool, which prints last N lines for a file provided as a param and watch for the new entries and print them on stdout until interrupted (tail -f -n N equivalent).

import argparse
import sys



def parse_args():
    print("hello")
    parser = argparse.ArgumentParser(description='Optional app description')

    parser.add_argument('path',
                    help='follow new entries')
    parser.add_argument('-n',
                    required = False,
                    type=int,
                    help='follow new entries')
    parser.add_argument('-f', '--follow',
                    required = False,
                    action='store_true',
                    help='follow new entries')

    args = parser.parse_args()
    return args.path, args.follow, args.n

def tail(path, follow, lines):
    fd = open(path)
    file_splitted_by_lines = fd.readlines() # array of lines
    number_lines = len(file_splitted_by_lines)
    
    last_lines = file_splitted_by_lines[number_lines-10:number_lines]
    
    for line in last_lines:
        print(line, end='')
    
    if (follow):
        while(True):
            try:
                new_content = fd.read()
                print(new_content, end='')
            except KeyboardInterrupt:
                fd.close()
                sys.exit(0)
    else:
        fd.close()

def main():
    path, follow, lines = parse_args()
    tail(path, follow, lines)

if __name__ == "__main__":
    main()

