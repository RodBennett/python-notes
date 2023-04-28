# ACCEPTING ARGUMENTS FROM COMMAND LINE

import sys

# index [1] is the value, index[0] is name of file cli_agrs.py
name = sys.argv[1]
print("Hello " + name)

import argparse

parser = argparse.ArgumentParser(
    description="This arg prints name of dogs"
)

parser.add_argument("-c", "--color", 
                    metavar="color", 
                    required=True, 
                    choices={"red", "yellow"},
                    help="the color to search for")

args = parser.parse_args()

print(args.color)