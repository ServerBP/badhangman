import random
import os
from os import sys
import guess_given as guess_given

lines = []
guesses = []
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
newguess = input("We have chosen a word. This word is " + str(wlength) + " characters long. Take your first guess: ")
print(initialword)

# player takes their first guess
if len(newguess) != 1:  # checking if its the correct character count
    print("Please try again. You may only guess 1 character at a time")
guess_given.guess(newguess, initialword, current_status, guesses)

input_correct_format = False

while flag == 0:
    while input_correct_format == False:
        newguess = input("Take a guess (another character): ")
        if len(newguess) != 1:  # checking if its the correct character count
            print("Please try again. You may only guess 1 character at a time")
        current_status = guess_given.guess(newguess, initialword, current_status, guesses)

