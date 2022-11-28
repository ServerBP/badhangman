import random
import os
from os import sys
import guess_given as guess_given
import listupdate as listupdate

lines = []
guesses = []
correct_g = []
incorrect_g = []
incorrect_amount = 0
newguess = ""
current_status = {}

with open(os.path.join(sys.path[0], "magyar_latin2.txt"), "r") as file:  # read file
    lines = [line.rstrip() for line in file]  # make all lines into an argument in the list

initialword = random.choice(lines)  # choose the inital word and make it a variable
wlength = len(initialword)  # the length of the inital word which we will be sticking to
list_of_available = []

for word in lines:  # run through all words in the initial list
    if len(word) == wlength:  # filter all words from the initial list that are the same character length as the initial word
        list_of_available.append(word)  # if it is the same length then add it to a new list

# startup info given to user
print("Bad akasztofa game \nTry to guess the word by guessing characters 1 by 1.")
# player takes their first guess
newguess = input("We have chosen a word. This word is " + str(wlength) + " characters long. Take your first guess: ")
print(initialword)
if len(newguess) != 1:  # checking if its the correct character count
    print("Please try again. You may only guess 1 character at a time")
