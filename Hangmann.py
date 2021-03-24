


import random
from time import sleep
from Hangman_parts import parts

with open("words_list", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))

picked = (random.choice(words))
print(picked)

def update():
    for i in right:
        print(i, end=" ")
    print()

def wait():
    for i in range(5):
        print(".", end="")
        sleep(.3)
    print()

print("Hi! Let´s play hangman")
print("I have chosen a word")
wait()
print("The word has:", len(picked), "letters")

right = ["_"] * len(picked)
wrong = []

wait()

update()
parts(len(wrong))

while True:
    print("===============================")
    guess = input("Guess a letter: ")
    print("let me check")
    wait()

    if guess in picked:
        index = 0
        for i in picked:
            if i == guess:
                right[index] = guess
            index += 1
        update()
        print("correct")

    else:
        if guess not in wrong:
            wrong.append(guess)
            parts(len(wrong))
            print("sorry, that is not it! Try again")
        else:
            print("you have already picked that")
    print(wrong)

    if len(wrong) > 4:
        print("You Lose")
        print("i picked: ", picked)
        break
    if "_" not in right:
        print("You win!")
        wait()
        break
file.close()
