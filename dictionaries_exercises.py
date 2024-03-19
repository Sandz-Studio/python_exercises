# Q1
# The dictionary below represents the cost of individual items in a supermarket. Write a
# program that asks the user how many of each item they would like in turn, and outputs
# the total cost of their groceries.

groceries = {
"Baby Spinach": 2.78,
"Hot Chocolate": 3.70,
"Crackers": 2.10,
"Coffee": 9.00,
"Carrots": 0.56,
"Oranges": 3.08
}

totals = []

for key, value in groceries.items():
    amounts = int(input(f"How many {key} would you like: ")) * value
    grocery_total = totals.append(amounts)
    grocery_sum = sum(totals)
    

print(f"Thankyou, your total is ${grocery_sum}")










# come back ro these exercises later when you have time.

# ingredients = {
# "Mixed Soaked Fruit": "200g",
# "Flour": "400g",
# "Baking Powder": "1tsp",
# "Ground Cinnamon": "0.5tsp",
# "Ground Ginger": "0.5tsp",
# "Ground Nutmeg": "1 pinch",
# "Salt": "0.5tsp",
# "Butter": "200g",
# "Sugar": "50g",
# "Eggs": 4
# }
# for key, value in ingredients.items():
#     print(f"Ingredient: {key}, Quantity: {value}")