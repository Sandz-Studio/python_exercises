# List
# ingredients = [
# "Mixed Soaked Fruit",
# "Flour",
# "Baking Powder",
# "Ground Cinnamon",
# "Ground Ginger",
# "Ground Nutmeg",
# "Salt",
# "Butter",
# "Sugar",
# "Eggs"
# ]


# # Dictionary
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


# # Value can be any data type
# mixed_dict = {
# "integer": 3,
# "float": 4.0,
# "string": "Hello world!",
# "boolean": True,
# "none": None,
# "list": [1, "a", False],
# "dictionary": {"a": 1, "b": 2, "c": 3}
# }





# # Example where keys are all different data types
# dict_mixed = {
# "abc": "A string",
# 1: "An integer",
# 2.0: "A float",
# False: "A boolean",
# None: "None"
# }




# # Accessing Values 
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
# # Accessing the value with square bracket notation.
# flour_amount = ingredients["Flour"]

# print(f"To bake this fruitcake you need {flour_amount} grams of flour.")





# # Storing values 
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

# ingredients["Pecans"] = "25g"

# print(ingredients)



# # We can also overwrite the existing values in the dictionary in exactly the same way:
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
# print(ingredients)
# print("That's way too much flour!")
# ingredients["Flour"] = "200g"
# print(ingredients)




# # Deleting from a dictionary
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
# print(ingredients)

# print("I'm allergic to nutmeg...")

# del ingredients["Baking Powder"]

# print(ingredients)






# # ITERATING OVER DICTIONARIES 
# # .keys()
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
# for key in ingredients.keys():
#     print(key)



# # .values
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
# for value in ingredients.values():
#     print(value)





# .items()
# loop through each key/value pair in the dictionary
ingredients = {
"Mixed Soaked Fruit": "200g",
"Flour": "400g",
"Baking Powder": "1tsp",
"Ground Cinnamon": "0.5tsp",
"Ground Ginger": "0.5tsp",
"Ground Nutmeg": "1 pinch",
"Salt": "0.5tsp",
"Butter": "200g",
"Sugar": "50g",
"Eggs": 4
}
for key, value in ingredients.items():
    print(f"Ingredient: {key}, Quantity: {value}")