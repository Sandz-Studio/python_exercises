# # # colours_20_simple file
# import csv

# with open("csv_files/colours_20_simple.csv", encoding="utf-8") as my_file:
    
#     reader = csv.reader(my_file)
#     reader_list = list(reader)



# Q1
# Write a program that reads in colours_20_simple.csv and print each line of the colour
# data one by one as a string. Use spaces to separate the columns insead of commas.

# for line in reader_list:
#         print(" ".join (line))

        


# Q2
# Write a program that reads in colours_20_simple.csv and outputs the colour data in
# order English, Hex then RGB, like so:

# for line in reader_list:
#     print(sorted(line, reverse=True))




# # # Q3/PT1
# # # Write a program that takes a csv file describing colours, and outputs the number of
# # # times each of the following colours appears in the English Name:

#     red_count = 0
#     green_count = 0
#     blue_count = 0
#     yellow_count = 0


#     for line in reader_list:
#         colour = line[2]
#         if "red" in colour:
#             red_count += 1
#         if "green" in colour:
#             green_count += 1
#         if "blue" in colour:
#             blue_count += 1
#         if "yellow" in colour:
#             yellow_count += 1
     

#     print(f"Red: {red_count} Green: {green_count} Blue: {blue_count} Yellow: {yellow_count}")






# # colours_865 File
# import csv

# with open("csv_files/colours_865.csv", encoding="utf-8") as my_file:
    
#     reader = csv.reader(my_file)
#     reader_list = list(reader)   

# # Q3/PT2
#     red_count = 0
#     green_count = 0
#     blue_count = 0
#     yellow_count = 0
#     orange_count = 0
#     white_count = 0
#     grey_count = 0
#     pink_count = 0
#     black_count = 0
#     brown_count = 0


#     for line in reader_list:
#         colour = line[2]
#         if "Red" in colour:
#             red_count += 1
#         if "Green" in colour:
#             green_count += 1
#         if "Blue" in colour:
#             blue_count += 1
#         if "Yellow" in colour:
#             yellow_count += 1
#         if "Orange" in colour:
#             orange_count += 1
#         if "White" in colour:
#             white_count += 1
#         if "Grey" in colour:
#             grey_count += 1
#         if "Pink" in colour:
#             pink_count += 1
#         if "Black" in colour:
#             black_count += 1
#         if "Brown" in colour:
#             brown_count += 1
     

#     print(f"Red: {red_count} Green: {green_count} Blue: {blue_count} Yellow: {yellow_count} Orange: {orange_count} White: {white_count} Grey: {grey_count} Pink: {pink_count} Black: {black_count} Brown: {brown_count}")








# Using galaxies csv file
# Q4
# galaxies.csv contains data about 82 different galaxies and their velocities (km/sec).
# Using this data, print a string showing the galaxy with the slowest velocity, and
# another showing the galaxy with the highest velocity.

galaxy_velocities = []

import csv

with open("csv_files/galaxies.csv") as my_file:
    
    reader = csv.reader(my_file)
    # reader_list = list(reader)
    for line in reader:
        galaxy_velocities.append(int(line[1]))

# All of this is not needed! can do sinmple min/max funtion to the appended galaxy_velocitieds list!
    # min_vel = galaxy_velocities[0]
    # max_vel = galaxy_velocities[0]
    
    #  # could for for statement 
    # for number in galaxy_velocities:
    #         # if number < min_vel:
    #         #      smallest = number
    #         if number > max_vel:
    #              largest = number
    
    # print(f"Smallest velocity: {min_vel} Largest velocity: {max_vel}")
    
    print(f"Slowest Velocity: {min(galaxy_velocities)}")
    print(f"Highest Velocity: {max(galaxy_velocities)}")
    



# # Karen's Solution!

# import csv
# with open("csv files\\galaxies.csv", encoding="utf-8") as my_file:
#     reader = csv.reader(my_file)
#     galaxies = list(reader)
#     min_galaxy = galaxies[0]
#     max_galaxy = galaxies[0]
#     for galaxy in galaxies[1:]:
#         if int(galaxy[1]) < int(min_galaxy[1]):
#             min_galaxy = galaxy
#         if int(galaxy[1]) > int(max_galaxy[1]):
#             max_galaxy = galaxy
#     print(f"Galaxy {min_galaxy[0]} has the min velocity of {min_galaxy[1]}km/sec.")
#     print(f"Galaxy {max_galaxy[0]} has the max velocity of {max_galaxy[1]}km/sec.")
#     print()
#     print(f"Galaxy {min_galaxy[0]} has the min velocity of {min_galaxy[1]}km/sec.\nGalaxy {max_galaxy[0]} has the max velocity of {max_galaxy[1]}km/sec.")
