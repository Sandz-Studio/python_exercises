# my_num = 1

# def my_function():
#     my_num = 2
#     return my_num

# print(my_function())









# def my_function():
#     return "Hello"

# print(my_function())









# my_num = 1

# def my_function():
#     my_num = input()
#     return my_num

# print(my_function())








# my_num = 1

# def my_function():
#     my_num = 2
#     return my_num

# another_num = my_function()
# print(another_num)













# Workbook


# def calculate_mean(num1, num2):
#     mean = (num1 + num2)/2
#     return mean

# avg = calculate_mean(30, 20)

# print(avg)






# # Returning Is Optional

# def greeting_function(some_name):
#     print(f"Hi {some_name}, it's great to see you!")

# mysterious_value = greeting_function("Oliver")

# print(mysterious_value)






# # Parameters Are Also Optional

# def get_int():
#     the_int = int(input("Give me an integer, please."))
#     return the_int

# user_input = get_int()





# # Global Scope

# global_value = 3

# print(f"Outside of the function, global_value = {global_value}.")

# def my_function():
#     print(f"Inside of the function, global_value = {global_value}.")

# # Have to execute the function or the code inside it won't run!
#     my_function()
#     print(f"After the function, global_value = {global_value}.")








# # Local scope

# def private_function():
#     local_value = 42
#     print(f"Inside of the function, local_value = {local_value}.")

# private_function()

# print(f"After of the function, local_value = {local_value}.")









# # Namespace Heirarchy
# # Global Namespace
# the_value = 0 

# print(f"Before the function, the_value = {the_value}.")

# def another_function():
#     # Local Namespace
#     the_value = 999
#     print(f"Inside the function, the_value = {the_value}.")

# another_function()

# # Global Namespace
# print(f"After the function, the_value = {the_value}.")











# DON'T modify global value from inside a function
my_value = 50

print(f"before the function, my_value = {my_value}")

# We tell our function to expect a parameter
def generate_new_value(val_to_mod):
    # We modify the parameter and return the new value
    return val_to_mod + 8951

# We assign the result of our function as the new value for our global variable

my_value = generate_new_value(my_value)

print(f"after the function, my_value = {my_value}")

