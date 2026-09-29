import random

words = ["python", "laptop", "coding", "network", "keyboard"]
word = random.choice(words)

guessed = []
wrong_letters = []
max_wrong = 6

print("Welcome to Hangman!")
print("The word has", len(word), "letters. You get", max_wrong, "wrong guesses.")

while len(wrong_letters) < max_wrong:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong letters:", " ".join(wrong_letters))
    print("Guesses left:", max_wrong - len(wrong_letters))

    if "_" not in display:
        print("Congratulations, you won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed or guess in wrong_letters:
        print("You already guessed that letter.")
        continue

    if guess in word:
        guessed.append(guess)
        print("Good guess!")
    else:
        wrong_letters.append(guess)
        print("Wrong guess!")
else:
    print("\nGame over! The word was:", word)