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

# def rock_paper_scissors(n):
#   # return an array
#   outcomes = []
#   # we don't have a list of possible plays
#   plays = ['rock', 'paper', 'scissors']

#   # generate an n-length permutation of possible plays
#   # in case when n == 0
#   # move towards our base by decrementing n
#   # every time we decrement n, we'll add another possible play to the list we're get

#   # define an inner recursive helper function
#   def generate_plays(rounds_left, result=[]):
#     if rounds_left = 0:
#       outcomes.append(result)
#       return
#     for play in plays:
#       generate_plays(rounds_left -1, result + [play])
#   generate_plays(n, [])
#   return outcomes

if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python rps.py [n]` with different n values
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')