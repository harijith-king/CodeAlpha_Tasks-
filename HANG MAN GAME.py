import random

words = ["python", "array", "string", "random", "loop"]
word = random.choice(words)
guessed = ["_"] * len(word)
used = []
chances = 6

while chances > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Used letters:", " ".join(used))
    print("Chances left:", chances)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single valid letter")
        continue

    if guess in used:
        print("Already guessed")
        continue

    used.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct guess")
    else:
        chances -= 1
        print("Wrong guess")

if "_" not in guessed:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost! The word was:", word)
