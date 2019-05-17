import argparse

parser = argparse.ArgumentParser(description="A script to demonstrate the use of the argparse library in Python")
parser.add_argument("--cmd_name", dest="variable_name", help="Help for this arg")
parser.add_argument("--iter", type=int)
args = parser.parse_args()

if args.variable_name is not None:
    print("Arg set")
