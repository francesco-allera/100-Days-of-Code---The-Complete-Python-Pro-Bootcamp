# # For Loops:
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
# print(fruits)


# # Practice:
# student_scores = [180, 124, 165, 173, 189, 169, 146]

# total_exam_score = sum(student_scores)
# print(total_exam_score)
# total = 0
# for score in student_scores:
#     total += score
# print(total)

# highest_exam_score = max(student_scores)
# print(highest_exam_score)
# highest = 0
# for score in student_scores:
#     if score > highest:
#         highest = score
# print(highest)


# # Range function:
# print('range: ', range(1, 10))
# for number in range(1, 10):
#     print(number)
# for number in range(1, 20, 3):
#     print(number)
#
# sum = 0
# for number in range(1, 101):
#     sum += number
# print(sum)


# # #
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

chars = []
for _ in range(0, nr_letters):
    chars.append(random.choice(letters))
for _ in range(0, nr_numbers):
    chars.append(random.choice(numbers))
for _ in range(0, nr_symbols):
    chars.append(random.choice(symbols))
random.shuffle(chars)

password = ''
for _ in chars:
    password += _
print(password)
