class Cow():
    species_name = "Bos Taurus"
    diet = "grass"

    def __init__(self, instance_name, instance_colour):
        self.name = instance_name
        self.colour = instance_colour

    def __str__(self):
        return f"<A cow named {self.name}>"

    def speak(self):
        print("MOO!")

    # This is how you should mutate state in object
    def dye_hair(self, new_colour):
        self.colour = new_colour

bessie = Cow("Bessie", "Brown")
# cow1 = Cow("Daisy", "Black")
# cow2 = Cow("Nellie", "White")
# cow3 = Cow("Bessie", "Brown")


print(bessie)
# print("Say something Bessie!")
# bessie.speak()



# bessie.dye_hair("Rainbow")

# print(f"This cow's name is {bessie.name}.")
# print(f"{bessie.name} is {bessie.colour}.")



# # This is not the best way to mutate the state in an object
# print("Dyeing Bessie's hair...")
# bessie.colour = "Blue"
# print(f"{bessie.name} is {bessie.colour}.")





# print(f"This cow's name is {cow1.name}.")
# print(f"{cow1.name} is {cow1.colour}.")
# print(f"{cow1.name} eats {cow1.diet}.")

# print(f"This cow's name is {cow2.name}.")
# print(f"{cow2.name} is {cow2.colour}.")
# print(f"{cow2.name} eats {cow2.diet}.")

# print(f"This cow's name is {cow3.name}.")
# print(f"{cow3.name} is {cow3.colour}.")
# print(f"{cow3.name} eats {cow3.diet}.")