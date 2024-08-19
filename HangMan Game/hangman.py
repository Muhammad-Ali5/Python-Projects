import random
print("==> Welcome to Hangman Game <==")
print("-------------------------------")
word_list=["python","kotlin","java","javascript","react"]
random_word=random.choice(word_list)
blank_space=["_"] *len(random_word)
guesses=6

while (guesses>0):
    print(" ".join(blank_space))
    guess=input("Guess the letter : ").lower()
    if guess in random_word:
        for i, letter in enumerate(random_word):
            if letter==guess:
                blank_space[i]=guess
    else:
        guesses -=1
        print(f"Incorrect! And the {guesses} Guess are remaining...")

    if "_"not in blank_space:
        print("-------------------------------")
        print("Congratulation ! You won ...")
        print(f"The Word is : {random_word}")
        print("-------------------------------")
        break
else:
    print(f"Sorry you lose! the word are : {random_word}")