#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  options = [['rock'], ['paper'], ['scissors']]
  result = []
  if n==0:
    return result
  if n>0:
    def recursion(possibilities):
      if len(possibilities) == n:
        result.append(possibilities)
        return
      for p in options:
        recursion(possibilities + p)
    recursion([])
    return result

if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python rps.py [n]` with different n values
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')