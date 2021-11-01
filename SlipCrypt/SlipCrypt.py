#!/usr/bin/python3
from core.program import program
from sys import exit

program = program()

if __name__ == '__main__':
    try:
        program.SlipCrypt()
    except KeyboardInterrupt:
        exit('\n[!] Quitting...')