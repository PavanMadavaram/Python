#Day 83 - Test
import argparse
import sys
sys.argv = ['test.py', 'test']
parser = argparse.ArgumentParser()
parser.add_argument('test')
args = parser.parse_args()
print("Argparse test:", args.test == 'test')
print("Day 83 test ok")