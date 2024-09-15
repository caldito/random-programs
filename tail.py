#!/usr/bin/env bash

# Implement a tail(1)-like tool, which prints last N lines for a file provided as a param and watch for the new entries and print them on stdout until interrupted (tail -f -n N equivalent).

import sys

def main(path,follow):
    fd = open(path)
    file_splitted_by_lines = fd.readlines() # array of lines
    number_lines = len(file_splitted_by_lines)
    
    last_lines = file_splitted_by_lines[number_lines-10:number_lines]
    
    for line in last_lines:
        print(line)
    
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
        

