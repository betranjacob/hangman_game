import random
import string

FILE_NAME = 'words.txt'
NUMBER_OF_GUESSES = 9


def clean_word(word):
    # Filter for well-formed word.
    # Ignore any tokens that contain punctuation.
    NUMBERS = '1234567890'
    if len(word) > NUMBER_OF_GUESSES:
        return

    for symbol in string.punctuation:
        if symbol in word:
            return
    # ignore any tokens that have numbers in them
    for number in NUMBERS:
        if number in word:
            return
    return word.lower()


def get_words_from_file(filename=FILE_NAME):
    """
    :param filename: Read all words from the given file
    :return: list of unique words
    """
    with open(filename, 'r') as f:
        words_list = set()
        all_words = f.read()
        all_words = all_words.split(' ')
        for word in all_words:
            cword = clean_word(word)
            if cword:
                words_list.add(cword)
    return list(words_list)


def update_dashes(secret, cur_dash, rec_guess):
    """
    This function updates the string of dashes by replacing the dashes
    with words that match up with the hidden word if the user manages to guess
    it correctly
    :param secret:
    :param cur_dash:
    :param rec_guess:
    :return:
    """
    result = ""
    for i in range(len(secret)):
        if secret[i] == rec_guess:
            # Adds guess to string if guess is correctly
            result = result + rec_guess
        else:
            # Add the dash at index i to result if it doesn't match the guess
            result = result + cur_dash[i]

    return result


def play_hangman(secret_word):

    print(secret_word)
    print("Welcome to Hangman Game")
    print('The secret word has {} letters'.format(len(secret_word)))
    # Set the dashes to the length of the secret word and set the amount of guesses to 9
    dashes = "-" * len(secret_word)
    guesses_left = NUMBER_OF_GUESSES

    while guesses_left > 0 and not dashes == secret_word:

        # Print the amount of dashes and guesses left
        print(" ".join(dashes))
        print('guesses_left: ', str(guesses_left))

        guess = input("Guess a letter or the whole word:")
        if guess == secret_word:
            print("Excellent! You guessed the whole word correctly! The word was: " + str(secret_word))
            return

        # Conditions that will print out a message according to invalid input.
        elif len(guess) != 1:
            print("Your guess must have exactly one character or the whole word")

        # If the guess is in the secret word then we update dashes to replace the
        # corresponding dash with the correct index the guess belongs to in the
        # secret word
        elif guess in secret_word:
            print("That letter is in the secret word!")
            dashes = update_dashes(secret_word, dashes, guess)

        # If the guess is wrong then we display a message.
        else:
            print("That letter is not in the secret word!")

        # For every guess subtract the amount of guesses the user has by 1
        guesses_left -= 1

    if guesses_left == 0:
        print ("You lose. The word was: " + str(secret_word))
    else:
        print("Congrats! You win. The word was: " + str(secret_word))


if __name__ == '__main__':
    words = get_words_from_file()
    print(len(words))
    play_hangman(random.choice(words))