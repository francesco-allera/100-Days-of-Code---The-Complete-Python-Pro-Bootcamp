# # Primitive Data Types:
# # Subscripting
# print("Hello"[0])
# print("Hello"[4])
# print("Hello"[-1])
# print("Hello"[-2])

# # String
# print("123" + "345")

# # Integer
# print(123 + 345)

# # Large Integers
# print(123_456_789)

# # Float
# print(3.14159)

# # Boolean
# print(True)
# print(False)


# # Type Checking:
# print(type("Hello"))
# print(type(12345))
# print(type(3.14159))
# print(type(True))


# # Type Conversion:
# print(int("123") + int("456"))
# print(float(123))
# print(str(123))
# print(bool(123))
# print(bool(0))
# print(bool("ok"))
# print(bool(""))

# name_of_the_user = input("Enter your name: ")
# length_of_name = len(name_of_the_user)
# print("Number of letters in your name: " + str(length_of_name))


# Mathematical Operations:
# print(123 + 456)
# print(7 - 3)
# print(3 * 2)
# print(5 / 3)
# print(5 // 3)
# print(2 ** 3)

# # PEMDAS
# print(3 * 3 + 3 / 3 - 3)


# # Number Manipulation:
# height = 1.65
# weight = 84
# bmi = weight / height**2
# print(int(bmi))
# print(round(bmi))
# print(round(3.7))
# print(round(3.4))
# print(round(bmi, 2))

# score = 0
# score += 5
# print(score)
# score -= 1
# print(score)
# score /= 2
# print(score)
# score *= 3
# print(score)

# # f Strings:
# print("Your score is " + str(score))
# height = 1.8
# is_winning = True
# print(f"Your score is {score}, your height is {height}, and your winning is {is_winning}")


# # #
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total = bill * (1 + tip / 100) / people
print(f"Each person should pay: ${round(total, 2)}")
