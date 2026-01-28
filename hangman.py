import random

words = ["apple", "banana", "mango", "orange", "grapes"]
word = random.choice(words)

guessed_letters = []
tries = 6
display = ["_"] * len(word)

print("🎮 Welcome to Hangman Game")

while tries > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Correct guess!")
    else:
        tries -= 1
        print("Wrong guess! Tries left:", tries)

if "_" not in display:
    print("\n🎉 You won! The word was:", word)
else:
    print("\n😢 You lost! The word was:", word)
