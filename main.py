import random
import os
from os import sys
import guess_given as gg

lines = []
guesses = []
correct_guesses = []
incorrect_amount = 0
newguess = ""
current_status = {}
flag = 0

with open(os.path.join(sys.path[0], "magyar_latin2.txt"), "r") as file:  # read file
    lines = [line.rstrip() for line in file]  # make all lines into an argument in the list

initialword = random.choice(lines)  # choose the inital word and make it a variable
wlength = len(initialword)  # the length of the inital word which we will be sticking to
list_of_available = []

for word in lines:  # run through all words in the initial list
    if len(word) == wlength:  # filter all words from the initial list that are the same character length as the initial word
        list_of_available.append(word)  # if it is the same length then add it to a new list

for index in range(len(initialword)):
    current_status.update({index: '_'})
print(current_status)

# startup info given to user
print("Bad akasztofa game \nTry to guess the word by guessing characters 1 by 1.")
print(initialword)
print("We have chosen a word. This word is " + str(wlength) + " characters long. lets start the game by you guessing a letter!")


input_correct_format = False

while flag == 0:
    while input_correct_format == False:
        newguess = input("Your turn (guess a letter): ")
        if len(newguess) != 1:  # checking if its the correct character count
            print("Please try again. You may only guess 1 character at a time")
            break
        if newguess in initialword:
            cs2 = {}
            cs3 = current_status
            currentword = ""
            i = 0
            l= 0
            j = -1
            for i in list_of_available:
                j += 1
                currentWord = list_of_available[j]
                for index in range(len(currentWord)):
                    cs2.update({index: '_'})
                    indexes = [i for i, c in enumerate(initialword) if c == newguess]

                while l <= len(indexes)-1:
                    cs3.update({indexes[l]: newguess})
                    l = l+1
                while l <= len(indexes)-1:
                    cs2.update({indexes[l]: newguess})
                    l = l+1

                if cs2.values() != current_status.values():
                    list_of_available.remove(currentWord)
            print(list_of_available)
                
        msg, current_status, guesses, correct_guesses = gg.guess(newguess, initialword, current_status, guesses, correct_guesses)
        if msg == "err1":
            print("You have already guessed this letter. Try again!")
            break
