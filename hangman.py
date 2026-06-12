import random

# List of predefined words
words = ["python", "apple", "college", "coding", "laptop"]

# Select a random word
word = random.choice(words)

# Create blanks
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
attempts = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Guessed Letters:", ", ".join(guessed_letters))
    print("Remaining Attempts:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single alphabet letter.")
        continue

    # Check if letter already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if letter is in word
    if guess in word:
        print("✅ Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        print("❌ Wrong Guess!")
        attempts -= 1

# Game Result
print("\n--------------------")

if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over!")
    print("The word was:", word)