import random
import string
from FastText_guessing import guess as guess_word

def get_word():
    file_path = r'D:\ML_Projects\Hangman_Project\words_250000_train.txt'
    with open(file_path, 'r') as file:
        word_list = file.read().splitlines()

    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    correct_guesses = 0
    print("Let's play Hangman!")
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = guess_word(word)
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
                pass
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                correct_guesses += 1
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
                pass
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
                correct_guesses += 1
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
            pass
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
        pass
    else:
        print('correct guesses:', correct_guesses, 'total tries:', 6-tries)
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
        pass
    return correct_guesses, 6-tries

def main():
    game_count = int(input("How many times do you want the system to play the Hangman game?"))
    guess_stat = []
    for i in range(game_count):
        word = get_word()
        correct, tries = play(word)
        guess_stat.append((correct, tries))
    sum_correct = sum([i[0] for i in guess_stat])
    sum_tries = sum([i[1] for i in guess_stat])
    print(sum_correct, '/', sum_tries, '=', sum_correct/sum_tries)

if __name__ == "__main__":
    main()
