import random
from termcolor import colored


# I define a class for my word hunting game
class Word:
    # first, defines variables
    def __init__(self, game_mode, word_letter, word_list):
        self.g_mode = game_mode
        self.w_letter = word_letter
        self.w_list = word_list
        self.random_words = []
        if self.g_mode == 1:  # determines prediction number based on game mode
            self.predict_time = self.w_letter + 1
        else:
            self.predict_time = self.w_letter + (self.w_letter - 1)

    def random_word(self):  # it chooses words randomly in the number of game mode and particular word length
        for i in range(self.g_mode):
            self.random_words.append(random.choice(self.w_list))
        return self.random_words

    def gamer_inputs(self):  # it takes prediction inputs from user
        x = 0
        e_list = [["_" for j in range(self.w_letter)] for i in range(self.g_mode)]
        for i in range(self.g_mode):  # print the field which should be filled
            for j in e_list[0]:
                print(j, end="")
            print()
        i_str = ""
        print(colored("*", "blue") + "Write your prediction one by one (if you want to leave the game you should "
                                     "press the 0.)." + colored("*", "blue"))
        while x < self.w_letter:  # takes input up to word length
            a = input()
            if a.isalpha() and len(a) == 1:  # if input is okay, prints it in the area and puts it in the string
                for i in range(self.g_mode):
                    e_list[i][x] = a.upper()
                for i in range(self.g_mode):
                    for j in e_list[0]:
                        print(j, end="")
                    print()
                i_str += a.upper()
                x += 1
            elif a == "0":  # it means player wants to quit the game
                i_str = ""
                break
            else:  # if input is not appropriate asks again
                print(colored("!" * 3, "red") + "Please, write appropriate inputs(if you want to leave the game you "
                                                "should press the 0.)." + colored("!" * 3, "red"))

        return i_str  # returns the predicted word

    def word_control(self, r_random, i_str, copy_words):
        global b
        if i_str == "":
            self.predict_time = 0
            return ""
        for i in range(self.g_mode):  # controls predicted word in every word of the chosen ones
            b = True
            result_str = ""
            if r_random[i] == i_str:  # if the predicted word is matched with one of the chosen ones it comes here
                print(f"{i + 1}. word's prediction is true and the word is {r_random[i]}")
                # it removes that word from the copy list for the caution of same prediction
                copy_words.remove(r_random[i])
                b = False
                if copy_words == []:
                    # if the copy list is empty it means every word is predicted true and game should be done
                    self.predict_time = 1
                    print("You predict all the words true.")
            # if predicted word is not exactly same with the chosen words it controls every character
            else:
                for j in range(self.w_letter):
                    if r_random[i][j] == i_str[j]:
                        result_str += colored(i_str[j], "green")
                    elif r_random[i][j] != i_str[j] and (i_str[j] in r_random[i]):
                        result_str += colored(i_str[j], "yellow")
                    else:
                        result_str += colored(i_str[j], "red")
            if b:
                print(result_str)
        if b:
            print("(Letter color's meanings: Green--> True, Yellow--> Misplaced, Red--> Wrong)")
        self.predict_time -= 1
        while self.predict_time > 0:  # if predict time is bigger than 0 it goes to take input again
            a = self.gamer_inputs()
            if a == "":  # if empty string returns it means player wants to quit
                self.predict_time = 0
                return ""
            else:
                b = self.word_control(r_random, a, copy_words)
                if b == "":
                    return ""
        if self.predict_time <= 0:  # predict chances over and gives the last information
            if self.predict_time == 0:
                self.predict_time = -1
                for i in range(self.g_mode):
                    print(f"The {i + 1}. word is {r_random[i]}")
                print("Your predictions are(last to first):")
            print(f" {i_str}")
