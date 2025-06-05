# # Random Module:
# import random
# random_integer = random.randint(1, 10)
# print(random_integer)


# # Import our modules:
# import my_module
# print(my_module.my_favorite_number)


# # Some functions from random:
# import random
# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)
# random_number_0_to_10 = random.random() * 10
# print(random_number_0_to_10)
# random_float = random.uniform(1, 10)
# print(random_float)


# # Heads ot Tails:
# import random
# number = random.randint(0, 1)
# if number % 2 == 0:
#     print("Heads")
# else:
#     print("Tails")


# # Lists:
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# print(states_of_america[0])
# print(states_of_america[2])
# print(states_of_america[-1])
# print(states_of_america[-3])
# states_of_america[1] = "Pencilvania"
# print(states_of_america)
# states_of_america.append("JoJoland")
# print(states_of_america)
# states_of_america.extend(["State 1", "State 2"])
# print(states_of_america)


# # Who will pay the bill?
# import random
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# print(friends[random.randint(0, len(friends) - 1)])
# print(random.choice(friends))


# # IndexErrors:
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# num_of_states = len(states_of_america)
# print(states_of_america[num_of_states - 1])
# print(states_of_america[num_of_states])


# # Nested Lists:
# dirty_dozen = ["Celery", "Nectarines", "Spinach", "Grapes", "Apples", "Tomatoes", "Kale", "Peaches", "Pears", "Strawberries", "Cherries", "Potatoes"]
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)


# # #
import random
import ascii

user = int(input("What do you choose? "
                 "Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
cpu = random.randint(0, 2)

if 0 <= user <= 2:
    print("You chose:\n", ascii.game_images[user])
    print("Computer chose:\n", ascii.game_images[cpu])

if user < 0 or user > 2:
    print("You typed an invalid number. You lose!")
elif user == cpu:
    print("It's a Draw!")
elif (user == 0 and cpu == 2) or (user == 1 and cpu == 0) or (user == 2 and cpu == 1):
    print("You Win!")
else:
    print("You Lose!")