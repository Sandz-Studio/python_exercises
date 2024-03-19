# Q1
# Create a class to represent She Codes Students. Attributes that you may want to
# include: Name, Program, Year they attended

# Q2
# Add a __str__ method to your student class that returns a summary of the student's information.
# For a student named Olivia who attended Plus in 2019, it should look like:
# "<Student: Olivia, Program: Plus, Year: 2019>"

# class student():
#     org_name = "She Codes"

#     def __init__(self, instance_name, instance_program, instance_year):
#         self.name = instance_name
#         self.program = instance_program
#         self.year = instance_year
    
#     # Q2
#     def __str__(self):
#         return f"<Student:{self.name}, {self.org_name} Program:{self.program}, Year:{self.year}.>"
    

# student1 = student("Olivia", "Plus", "2023")

# print(student1)










# Q3
# Write a class that represents a rectangle shape and has a method for each of the
# following: Calculating the area, Calculating the perimeter, Calculating the length of the diagonal, Determining whether or not the rectangle is a square.

class rectangle():

    def __init__(self, instance_name, width, height):
        self.name = instance_name
        self.width = width
        self.height = height

    def __str__(self):
        return f"<A rectangle named {self.name}>"
    
    def calc_area(self, width, height):
        self.area = width * height
        return self.area
    
    def calc_perimiter(self, width, height):
        self.perimiter = (width + height) * 2
        return self.perimiter
    
    def calc_diagonal(self, width, height):
        self.diagonal = (width**0.5) + (height**0.5)
        return self.diagonal
    
    def calc_square(self, width, height):
        if width == height:
            return "This is a square"
            
        else:
            return "This is a rectangle"
        

        # The prints are not needed as the return acts like print - if there is no return then the function return NONE.
        #     print("This is a square")
        # else:
        #     print("This is a rectangle")
        # return ""
   
rec1 = rectangle("Rectangle 1", 100, 50)

# print(rec1.calc_square(100,100))
print(f"Area:{rec1.calc_area(100, 50)}")
print(f"Perimiter:{rec1.calc_perimiter(100, 50)}")
print(f"Diagonal Length:{rec1.calc_diagonal(100, 50)}")
print(f"Square or rectangle: {rec1.calc_square(100, 50)}")