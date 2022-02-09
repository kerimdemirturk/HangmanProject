import random

list_ = ['python', 'java', 'kotlin', 'javascript']
guess_word = random.choice(list_)
guess_word_set = set(guess_word)
guessed_word_hint = "-" * len(guess_word)
useless_letters = set()
letters = set()
tries = 8
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

print("H A N G M A N")
answer = (input('Type "play" to play the game, "exit" to quit: '))

while True:
    if answer == "play":
        while tries > 0 and guess_word_set != letters:
            print()
            guessed_word_hint = ''
            for word in guess_word:
                if word in letters:
                    guessed_word_hint += word
                else:
                    guessed_word_hint += "-"
            print(guessed_word_hint)
            letter = input("Input a letter: ")

            if len(letter) != 1:
                print("You should input a single letter")
            elif letter in letters or letter in useless_letters:
                print("You've already guessed this letter")
            elif letter not in alphabet:
                print('Please enter a lowercase English letter')
            elif letter not in guess_word_set:
                print("That letter doesn't appear in the word")
                tries -= 1
                if(tries > 1):
                  print("Your remaining guess are" + " " + str(tries))
                elif(tries == 1):
                  print("Your remaining guess is" + " " + str(tries))
                else:
                  print("You have no more guessing.")
                useless_letters.add(letter)
            elif letter.isupper():
                print("Please enter a lowercase English letter")
            else:
                letters.add(letter)

        if guess_word_set == letters:
            print(f'You guessed the word {guess_word}!')
            print('You survived!')
            print()
            break
        else:
            print('You lost!')
            print()
            break

    end_answer = (input('Type "play" to play the game, "exit" to quit: '))
    if end_answer == "exit":
        break
