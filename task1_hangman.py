import random

while True:
    words = ["apple", "tiger", "chair", "table", "plant"]
    word = random.choice(words)

    guessed = ["_"] * len(word)
    guessed[0] = word[0]   # hint reveal first letter

    attempts = 6
    used_letters = []

    print("\nWelcome to Hangman Game!")
    print("Hint: First letter is", word[0])
    print("Word has", len(word), "letters")

    while attempts > 0 and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        print("Attempts left:", attempts)
        print("Used letters:", used_letters)

        letter = input("Enter a letter: ").strip().lower()

        # input validation
        if not letter.isalpha() or len(letter) != 1:
            print("Enter only one letter!")
            continue

        if letter in used_letters:
            print("Already used!")
            continue

        if letter not in used_letters:
            
            used_letters.append(letter)

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
            print("✅ Correct guess!")
        else:
            attempts -= 1
            print("❌ Wrong guess!")

    # result
    if "_" not in guessed:
        print("\n🎉 You WON! Word was:", word)
    else:
        print("\n💀 You LOST! Word was:", word)

    # replay option
    choice = input("Do you want to play again? (y/n): ").lower()

    if choice != "y":
        print("Thanks for playing!")
        break