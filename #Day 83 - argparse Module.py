#Day 83 - argparse Module 
import argparse

parser = argparse.ArgumentParser(description='Day 83 CLI Tool')
parser.add_argument('name', help='Your name')
parser.add_argument('-a', '--age', type=int, help='Your age')
parser.add_argument('--verbose', action='store_true', help='Verbose mode')

args = parser.parse_args(['Alice', '-a', '30', '--verbose'])
print(f"Hello {args.name}! Age: {args.age}, Verbose: {args.verbose}")