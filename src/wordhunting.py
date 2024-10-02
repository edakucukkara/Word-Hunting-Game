from termcolor import colored
from wordclass import Word


# ****************** file reading function ****************************************
# this function reads the words from the file and returns the lists for their words' lengths.
def read_words(w_file):
    l_4char = []
    l_5char = []
    l_6char = []
    f_read = open(w_file, "r", encoding="utf-8").readlines()
    for i in f_read:
        i_word = i.strip()
        if len(i_word) == 4:
            l_4char.append(i_word.upper())
        elif len(i_word) == 5:
            l_5char.append(i_word.upper())
        else:
            l_6char.append(i_word.upper())
    return l_4char, l_5char, l_6char


# ************************* exit line function ******************************
# This game is using same exit line in every exit so this is a function to use it when its needed
def finish_line():
    print(colored("*" * 24, "blue"))
    print("Okay, see you next time.")
    print(colored("*" * 24, "blue"))


# ********************* starting function ***********************************
# This is the first function to use in this function you will learn the game mode and word length from user.
def game_starting(e_game):
    start_sign = False  # This is a boolean value for understand the game is starting or not
    m_game = 0
    le_word = 0
    a_boolean = True
    while a_boolean:
        if not e_game:  # if it is the first game asks the player should game start
            print("Do you want to play ?(İf you want press the Y, if you don't press the N)")
            print(colored("*" * 72, "blue"))
            game_start = str(input())
        else:
            game_start = "Y"  # if it is not the first time you already accept playing the game
        if game_start.upper() == "Y":
            m_game = game_mode()  # learns the game mode
            if m_game == "0":  # if that function returns "0" it means player wants to finish the game
                a_boolean = False
            else:
                le_word = word_letter()  # learns the length of the word which will be predicted
                if le_word == "0":  # if that function returns "0" it means player wants to finish the game
                    a_boolean = False
                else:
                    print(colored("*", "blue") + "Game is beginning." + colored("*", "blue"))  # if every information
                    # has taken game can start
                    a_boolean = False
                    start_sign = True
        elif game_start.upper() == "N":  # if it is "N" that means player don't want to play
            a_boolean = False
        else:  # if input is not one of the given characters it asks again
            print(colored("!"*3, "red") + "Please send the appropriate character.(İf you want to play press the Y, "
                                          "if you don't press the N)" + colored("!"*3, "red"))
            a_boolean = True

    return start_sign, int(m_game), int(le_word)


# ************** game mode function ******************
# This is a function for learning the game mode from player.
def game_mode():
    result_mode = "0"
    a_boolean = True
    print(colored("*", "blue")+"This game has two game mode. 1 word mode and 4 word mode.(Press 1 or 4 and if you "
                               "want to exit press 0.)"+colored("*", "blue"))
    while a_boolean:
        given_mode = input()
        a_boolean = False  # if 1, 4 or 0 is given there is no need to turn again because these answers appropriate
        if given_mode == "1":
            result_mode = "1"
        elif given_mode == "4":
            result_mode = "4"
        elif given_mode == "0":
            result_mode = "0"
        else:  # if another thing is given then it asks again
            print(colored("!"*3, "red")+"Please send the appropriate character.(Press 1 or 4 and if you want to exit "
                                        "press 0.)"+colored("!"*3, "red"))
            a_boolean = True

    return result_mode


# ************************** word letter function ***********************************
# This is a function for learning how many letter should word have from player.
def word_letter():
    w_letter = "0"
    a_boolean = True
    print(colored("*", "blue")+"You can predict 4, 5 or 6 lettered word. Write which one you want(4, 5, 6 and if you "
                               "want to exit press 0)."+colored("*", "blue"))
    while a_boolean:
        n_letter = input()
        a_boolean = False  # if 4, 5, 6 or 0 is given there is no need to turn again because these answers appropriate
        if n_letter == "4":
            w_letter = "4"
        elif n_letter == "5":
            w_letter = "5"
        elif n_letter == "6":
            w_letter = "6"
        elif n_letter == "0":
            w_letter = "0"
        else:  # if another thing is given then it asks again
            print(colored("!"*3, "red")+"Please write one of the numbers that given (4, 5, 6 and if you want to exit "
                                        "press 0.)."+colored("!"*3, "red"))
            a_boolean = True

    return w_letter


# ******************************* needed list ********************************************
# it returns the list of words which is needed
def word_list(le_word):
    l_4, l_5, l_6 = read_words("words.txt")
    if le_word == 4:
        return l_4
    elif le_word == 5:
        return l_5
    else:
        return l_6


#######################################################################
# starting part
print(colored("*"*72, "blue"))
print("Hello, this is a game called Word Hunting.")

repeated_game = False
while True:
    e_boolean, g_mode, l_word = game_starting(repeated_game)  # learns the values
    if e_boolean:
        a = Word(g_mode, l_word, word_list(l_word))  # call the class
        words = a.random_word()  # gets the random words
        copy_words = words.copy()  # takes copy of random words
        input_str = a.gamer_inputs()  # gets the predictions
        if input_str == "":
            finish_line()  # if player wants to exit give the exit line
            break
        else:
            b = a.word_control(words, input_str, copy_words)  # control the characters
            if b != "":
                print(colored("*" * 72, "blue"))
                print("Do you want to play again?('Y' for yes or press anything for exit.)")
                print(colored("*" * 67, "blue"))
                if input().upper() == "Y":  # it asks for a new game
                    repeated_game = True
                else:
                    finish_line()
                    break
            else:
                finish_line()
                break
    else:
        finish_line()
        break
