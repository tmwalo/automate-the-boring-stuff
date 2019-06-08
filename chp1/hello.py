# This program says hello and asks for my name.

print("Hello world!")
print("What is your name?") # Ask for their name.
my_name = input()
print("It is good to meet you, " + my_name)
print("The length of your name is: ")
print(len(my_name))
print("What is your age?") # Ask for their age.
my_age_str = input()
my_age_int = int(my_age_str)
print("You will be " + str(my_age_int + 1) + " in a year.")
