import random
from word_list import words

random_word = random.choice(words)
random_word1 = random_word
random_word = list(random_word)

letters_used = []
num_wrong = 0
display_word = ["_" for _ in random_word]


def show_display_word():
    print(" ".join(display_word))


def num_guesses_left():
    print(10 - num_wrong, "guesses left")


def process_guess(guess):
    global num_wrong
    if guess in letters_used:
        print("You already guessed that letter. Try again.")
    elif guess not in "abcdefghijklmnopqrstuvwxyz":
        print("Please enter a valid letter.")
    else:
        letters_used.append(guess)
        if guess in random_word:
            for index, letter in enumerate(random_word):
                if letter == guess:
                    display_word[index] = guess
            show_display_word()
        else:
            num_wrong += 1
            show_display_word()
    num_guesses_left()
    if "_" not in display_word:
        print("Correct!!!")
        print("You got it correct with", 10 - num_wrong, "guesses left")
        exit()


while True:
    if num_wrong == 10:
        print("You lose!!!")
        print("The word was:", random_word1)
        exit()
    else:
        guess = input("Input a letter: ").lower()
        process_guess(guess)
