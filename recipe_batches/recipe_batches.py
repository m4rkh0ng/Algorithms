#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # count = 0
  # for ingredient in ingredients:
  #   if ingredient in recipe:
  #     if ingredients[ingredient]-recipe[ingredient] > recipe[ingredient]:
  #       count += 1
  #       ingredients[ingredient] = ingredients[ingredient]-recipe[ingredient]
  # return count
  if set(recipe.keys()) != set(ingredients.keys()):
    return 0
  batches = {i: int(ingredients[i]/recipe[i]) if ingredients[i] >= recipe[i] else 0 for i in recipe.keys()}
  return min(batches.values())

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))