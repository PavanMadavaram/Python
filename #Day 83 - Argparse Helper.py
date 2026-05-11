#Day 83 - Argparse Helper
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', required=True, help='Input file')
parser.add_argument('-o', '--output', help='Output file')
parser.add_argument('--count', type=int, default=10, help='Line count')

# Simulate args
args = parser.parse_args(['--file', 'input.txt', '-o', 'output.txt', '--count', '5'])
print(f"File: {args.file}, Output: {args.output}, Count: {args.count}")