# # Q1
# # Write a function called get_integer that takes a string as its argument, and uses that
# # string to prompt the user to enter an integer. Your function should return the integer
# # supplied by the user.
# # Here's some starter code:

# prompt = input("Could I please have an integer?: ")
# user_input = prompt

# # Define your function here
# def get_integer(prompt):
#     user_input = get_integer(prompt)
#     return prompt

# print(f"So your integer is {user_input}? Thanks!")
    
    





# # Q2
# # Write a function called celcius_convert that takes a number representing the
# # temperature in Farenheit as its argument, and returns a float representing the
# # temperature in Celcius.

# degrees_f = 50

# # Define your function here
# def celcius_convert(degrees_f):
#     celsius = (degrees_f - 32) * 5/9
#     return celsius

# print(celcius_convert(degrees_f))











# # Q3
# # Write a function that accepts one argument (an integer) and returns True when that
# # argument is odd and False when that argument is even. You can use the same format
# # as the starter code in the previous exercise. Just remember - you're returning the
# # result, not printing it!

# # integer = int(input("Give me an integer:"))

# # def integer_result(integer):
# #     integer % 2 == 0
# #     return 
    

# integer = int(input("Give me an integer:"))

# def calculate_integer(integer):
#     # this is using a modulator operator to check if a number is divisible by 2
#     if integer % 2 == 0:
#         return("True")

#     else:
#         return("False")

# print(calculate_integer(integer))








# # Q4
# # Write a function that takes two arguments; the unit price of an item, and how many
# # units were purchased. Return the total cost as a string.
    
# price_per_unit = float(input("Price per unit: "))
# # [4.25, 3.79, 1.49]

# num_units = int(input("Number of units: "))
# # [3, 1, 7]

# def total_price(price_per_unit, num_units):
#     total_price = float(price_per_unit) * int(num_units)
#     return total_price


# print(total_price(price_per_unit, num_units))








