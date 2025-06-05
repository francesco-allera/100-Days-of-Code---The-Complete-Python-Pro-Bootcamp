"""
Conditional Operators:
> greater than
< less than
>= greater than or equal to
<= less than or equal to
== equal to
!= not equal to
"""

# # if / else:
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry you have to grow taller before you can ride.")


# Modulo Operator:
# print(10 % 5)
# print(10 % 3)

# number = int(input("What is the number you want to check? "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# # Nested if / elif
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         print("Please pay $5")
#     elif age < 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("Sorry you have to grow taller before you can ride.")


# Multiple if statements:
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         bill = 5
#         print("Child tickets are $5")
#     elif age < 18:
#         bill = 7
#         print("Youth tickets are $7")
#     else:
#         bill = 12
#         print("Adult tickets are $12")
#     wants_photo = input("Do you want to have a photo take? y for Yes, n for No\n")
#     if wants_photo == 'y':
#         bill += 3
#     print(f"Your final bill is {bill}")
# else:
#     print("Sorry you have to grow taller before you can ride.")


# Practice:
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# cost = 0
# if size == 's':
#     cost += 15
# elif size == 'm':
#     cost += 20
# elif size == 'l':
#     cost += 25
# else:
#     print("You typed the wrong inputs.")
# if pepperoni == 'y':
#     cost += 2
#     if size != 's':
#         cost += 1
# if extra_cheese == 'y':
#     cost += 1
# print(f"Your final bill is ${cost}.")


# # Logical Operators:
# a = 12
# print(a > 15)
# print(a > 10)
# print(a > 10 and a < 15)
# print(a > 15 and a < 13)

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# print(a > 10 or a < 10)

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# print(not a < 0)

# print(not True)
# print(not False)


# # Adding condition for midlife crisis:
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         bill = 5
#         print("Child tickets are $5")
#     elif age < 18:
#         bill = 7
#         print("Youth tickets are $7")
#     elif 45 <= age <= 55: # age >= 45 and age <= 55
#         bill = 0
#         print("Everything is going to be ok. Have a free ride on us")
#     else:
#         bill = 12
#         print("Adult tickets are $12")
#     wants_photo = input("Do you want to have a photo take? y for Yes, n for No\n")
#     if wants_photo == 'y':
#         bill += 3
#     print(f"Your final bill is {bill}")
# else:
#     print("Sorry you have to grow taller before you can ride.")


# # #
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice1 = input("You're at a cross road. Where do you want to go? "
                  "Type \"left\" or \"right\"\n").lower()
if choice1 == "left":
    choice2 = input("You've come to a lake. "
                    "There is an island in the middle of the lake. "
                    "Type \"wait\" to wait for a boat. "
                    "Type \"swim\" to swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "There is a house with 3 doors."
                        "One red, one yellow and one blue. "
                        "Which color do you choose?\n").lower()
        if choice3 == "yellow":
            print("You found the treasure. You Won!")
        elif choice3 == "red":
            print("It's a room full of fire. Game Over!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over!")
        else:
            print("You choose a door that doesn't exist. Game Over!")
    else:
        print("You got attacked by an angry trout. Game Over!")
else:
    print("You fell into a hole. Game Over!")
