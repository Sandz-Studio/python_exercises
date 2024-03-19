# While Loop Exercises

# Q1
# Continuously ask the user to enter a number until they provide a blank input. Output
# the sum of all the numbers.

# num_list = []

# while True:
#     number = input("Enter a number:")

#     if number == "":
#         print(sum(num_list))
#         break

#     else:
#         num_list.append(int(number))




# # alternative solution
# sum_all_num = 0

# while (num := input("Enter a number")) !: "":
#     # summ_all_num += int(num)
#     sum_all_num = sum_all_num + int(num)

# print(f"Your numbers sum to {sum_all_num}.")
        











# Q2
# Ask the user to enter a in integer number. Print all the odd numbers between 0 and
# that number (inclusive). (Its ok not to worry about negative numbers for now, unless
# you really want a challenge.)

# number = input("Enter a number:")

# range = range(1, int(number) + 1, 2)

# list = list(range)

# print(list)



# use a modulus to print as alternative solution.










# Q3
# Write a guessing game.
# Select a number, and save it as a variable in your code. Ask the user to enter a
# number, and then output whether their number is less than or greater than the
# selected number. Keep asking until the user guesses the correct number. Then print a
# congratulatatory message.

# number = 9

# user_num = input("Guess the random number:")

# while int(user_num):
    
#     if int(user_num) == number:
#         print("You've got it right!") 
#         break

#     elif int(user_num) > number:
#         print("Too high...")
#         user_num = input("Guess the random number:")
    
#     elif int(user_num) < number:
#         print("Too low...")
#         user_num = input("Guess the random number:")







# For Loop Exercises

# Q1
# Ask the user for a number. Use a for loop to print the times tables for that number,
# up to ten:

# num = int(input("Enter a number:"))

# for a in range(10 + 1):
#     print(num * a)





# Q2
# Ask the user for an integer. Using a for loop, add up every number from 0 up to that
# integer, and print the result.

# num = int(input("Enter a number:"))

# list = list(range(int(num) + 1))

# for num in list:
#     print(sum(list))
#     break








# Q3
# Save a list of numbers to a variable in your script, and then use a for loop to print the
# sum of all the numbers in the list.

# num_list = [3,5,9,1]

# for a in num_list:
#     print(sum(num_list))
#     break









# Q4
# Let's improve our Mambo No. 5 code from the last block of content.
# Save the following variable in your code:

# lyrics = [
# ["Monica", "in my life"],
# ["Erica", "by my side"],
# ["Rita's", "all I need"],
# ["Tina's", "what I see"],
# ["Sandra", "in the sun"],
# ["Mary", "having fun"],
# ["Jessica", "here I am"]
# ]

# for a in lyrics:
#     print(f"A little bit of {a}")

# print("A little bit of you makes me your man (ah!)")
# print("*trumpet solo*")







# Extension Exercises
# Q1
# Below is a list of grocery items and their prices per unit:
# Ask the user how many units of each item they bought, then output the corresponding
# receipt. Here's an example of how that might look, but it's ok to change the text
# slightly in your code:

# groceries = [
# ["Baby Spinach", 2.78],
# ["Hot Chocolate", 3.70],
# ["BBQ Shapes", 9.00],
# ["Bread", 2.10],
# ["Carrots", 0.56],
# ["Oranges", 3.08]
# ]

# num_list = []

# for item in groceries:

#     num_0 = int(input(f"Please enter the quanity for {groceries[0][0]}:"))
#     num_1 = int(input(f"Please enter the quanity for {groceries[1][0]}:"))
#     num_2 = int(input(f"Please enter the quanity for {groceries[2][0]}:"))
#     num_3 = int(input(f"Please enter the quanity for {groceries[3][0]}:"))
#     num_4 = int(input(f"Please enter the quanity for {groceries[4][0]}:"))
#     num_5 = int(input(f"Please enter the quanity for {groceries[5][0]}:"))
#     break

# num_list.append(num_0)
# num_list.append(num_1)
# num_list.append(num_2)
# num_list.append(num_3)
# num_list.append(num_4)
# num_list.append(num_5)

# final_total = []

# for a in num_list:

#     total_0 = num_0 * groceries[0][1]
#     total_1 = num_1 * groceries[1][1]
#     total_2 = num_2 * groceries[2][1]
#     total_3 = num_3 * groceries[3][1]
#     total_4 = num_4 * groceries[4][1]
#     total_5 = num_5 * groceries[5][1]
#     break

# final_total.append(total_0)
# final_total.append(total_1)
# final_total.append(total_2)
# final_total.append(total_3)
# final_total.append(total_4)
# final_total.append(total_5)

# print(f"Your total is: {sum(final_total)}")







# Bridgets Solution - WAY MORE succinct but the total is not working?
groceries = [
["Baby Spinach", 2.78],
["Hot Chocolate", 3.70],
["BBQ Shapes", 9.00],
["Bread", 2.10],
["Carrots", 0.56],
["Oranges", 3.08]
]

total = 0

for item in groceries:
    total += float(input(f"Please enter the quantity for {item[0]}: ")) * item[1]

print(f" Thankyou, your total is ${total:,.2f}")















# Q2
# Let's improve the guessing game you wrote in Q3 of the while loop exercises. Update
# the code so that when the game ends, the program asks the player if they would like
# to play again. If they input "no" , the game ends, but with any other input the game
# begins again.
# Right now, your game will be a little busted, because the number the user has to guess
# will be the same every time. If you feel like challenging yourself even further, have a
# search around online - does Python give us a way to generate random numbers? This
# might involve using a new technique or two, so make sure you reach out to the
# mentors if you get stuck.
# Here's what the completed game might look like:



# # Bridgets Solution - A while loop within in while loop.
# import random

# print("Guess the random number!")

# keep_playing = True

# while keep_playing:
#     num = random.randint(0,10)

#     while (guess := int(input("make a guess:"))) != num:
#         if guess < num:
#             print("Too low...")
#         elif guess > num:
#             print("Too high...")
        
#     print("You got it right!")

#     if input("If you would like to stop playing, type 'no'. Otherwise, we'll play again: ") == "no":
#         keep_playing = False


        

