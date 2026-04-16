
       
# 1. Randomly choose a word from an array 
import random

words = ["apple","banana","laptop","mobile","bottle"]
chosen_word = random.choice(words);
print(chosen_word)
# 2. Ask the letter form the user 
# for loop run karna padega 

placeholder = "";

guess = input("Guess a letter: ");

word_length = len(chosen_word)
for position in range(word_length):
    print("This loop has run") 
    placeholder += "_";
print(placeholder)

for letter in chosen_word:
    if letter == guess:
        print("right");
    else:
        print("wrong");

