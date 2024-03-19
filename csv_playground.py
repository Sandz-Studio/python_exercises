import csv

with open("csv_files/colours_20_simple.csv", encoding="utf-8") as my_file:
    
    reader = csv.reader(my_file)
    reader_list = list(reader)

    # if you want to know thw row/cloumn numbert then you would use range
    for row in range(len(reader_list)):
          for column in reader_list[row]:
                print(f"Row: {row}, Column: {column}")

    # for line in reader:
    #     # for column in line:
    #         print(line)
    #         # print(column)
    #         # print(",".join(line))
    #         # print(line[2])


    # print(my_file)
    # do_stuff_function(my_file)


