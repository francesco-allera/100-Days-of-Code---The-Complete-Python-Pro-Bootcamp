# Hangman:
import random
import ascii, hangman_words

chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
for letter in chosen_word:
    placeholder += '_'
print(placeholder)

game_over = False
correct_letters = []
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed '{guess}'")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"You lose. The correct word was '{chosen_word}'.")

    if lives != 0:
        print(f"You have {lives} lives left.")

    print(f"Word to guess: display")
    print(ascii.stages[lives])

    if '_' not in display:
        game_over = True
        print("You win.")
