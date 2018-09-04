#!/usr/bin/python

import argparse

def find_max_profit(prices):
  return max(int(n) for n in prices)-min(int(n) for n in prices)

# alternatively, for what appears to be the intended solution:
# def find_max_profit(prices):
#   count = 0
#   profit = -100000
#   for lowest in prices:
#       count += 1
#       for highest in prices[count:]:
#         if highest-lowest > profit:
#           profit = highest-lowest
#   return profit

if __name__ == '__main__':
  # You can test your implementation by running 
  # `python stock_prices.py [prices]` where prices is comprised of
  # space-separated integer values
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

# in a list of integers, find the difference between the largest and the smallest values