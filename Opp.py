class user:
    def __init__(my, name, age, location):
        my.name = name
        my.age = age
        my.location = location

user = user("Vivian", 20, "Hoima")
#Create a new instance of user class    
print(user.name)
print(user.age)
#Create a function for the user class that prints user's location
def print_location(my):
          print("user's location:", my)
#Print the user's location using print_location function
print_location("Hoima")