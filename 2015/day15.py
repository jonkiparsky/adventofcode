"""
--- Day 15: Science for Hungry People ---
Today, you set out on the task of perfecting your milk-dunking cookie recipe.
All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a
list of the remaining ingredients you could use to finish the recipe (your
puzzle input) and their properties per teaspoon:

capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately, and you
have to be accurate so you can reproduce your results in the future. The total
score of a cookie can be found by adding up each of the properties (negative
totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon
(because the amounts of each ingredient must add up to 100) would result in a
cookie with the following properties:

A capacity of 44*-1 + 56*2 = 68
A durability of 44*-2 + 56*3 = 80
A flavor of 44*6 + 56*-2 = 152
A texture of 44*3 + 56*-1 = 76

Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now)
results in a total score of 62842880, which happens to be the best score
possible given these ingredients. If any properties had produced a negative
total, it would have instead become zero, causing the whole score to multiply to
zero.

Given the ingredients in your kitchen and their properties, what is the total
score of the highest-scoring cookie you can make?
 """


    


ingredients = """Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8""".split("\n")

ingredients_data = []


def row_data(row):
    _, data = row.split(": ")
    return [int(item.split(" ")[1]) for item in data.split(", ")]

ingredients = [row_data(row) for row in ingredients]

from math import prod

def compute_recipe_value_day_1(ingredients, qtys):
    interim = []
    for row, qty in zip(ingredients, qtys):
        interim.append([qty * n for n in row])
    rs = [sum(r) for r in zip(*interim)][:4]
    rs = [r  if r > 0 else 0 for r in rs]
    return prod(rs)


def check_calorie_count(ingredients, qtys):
    interim = []
    for row, qty in zip(ingredients, qtys):
        interim.append([qty * n for n in row])
    calorie_sum = sum([r[4] for r in interim])
    return calorie_sum == 500
    

def solve_day_1(ingredients):
    # brute force, there must be a nicer solution or why
    # does this problem exist?
    max_so_far = 0
    
    qty_iter = ntuples_summing_to(4,100)
    while True:
        try:
            qtys = next(qty_iter)
        except:
            break
        val = compute_recipe_value_day_1(ingredients, qtys)            
        max_so_far = max(val, max_so_far)
    return max_so_far
            
def solve_day_2(ingredients):
    # brute force, there must be a nicer solution or why
    # does this problem exist?
    max_so_far = 0
    
    qty_iter = ntuples_summing_to(4,100)
    while True:
        try:
            qtys = next(qty_iter)
        except:
            break
        val = compute_recipe_value_day_1(ingredients, qtys)
        if check_calorie_count(ingredients, qtys):        
            max_so_far = max(val, max_so_far)
    return max_so_far
            
    
from itertools import combinations, permutations
def ntuples_summing_to(n, _sum):
    combs = permutations(range(_sum), r=n)
    comb = next(combs)
    while True:
        while sum(comb) != _sum:
            try:
                comb = next(combs)
            except:
                raise StopIteration
        yield comb
        comb = next(combs)
        
        

test_ingredients = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3""".split("\n")

