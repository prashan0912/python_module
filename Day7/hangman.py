

def linear_search(guessed ,selected_word):
    flag = False
    for i in selected_word:
        # print(i,guessed)
        if(i==guessed):
            flag = True
            print("correct")
    if(flag):
        return 1    
    else:
        return 0

# import enumerate;
def change_update(selected_word,ans,guessed):
    for i,letter in enumerate(selected_word):
        # print(i,guessed,ans,letter)
        if guessed == i:
            ans[i]=guessed
            print(ans,letter)
            

def check_win(ans):
    for i,letter in enumerate(ans):
        if(ans[i] != "_"):
          print("win")
          return;


# 1. Randomly choose a word from an array 
import random

words = ["apple","banana","laptop","mobile","bottle"]
selected_word = random.choice(words);
print(selected_word)
# 2. Ask the letter form the user 
# for loop run karna padega 
life = 3
ans = "______"

if(life>0):
    while(life>0):
      guessed = input("Enter Gussed word: ")
      if(linear_search(guessed,selected_word)):
        life+=1
        print(life)
        change_update(selected_word,ans,guessed)
        print("right")
        check_win(ans);
      else:
          life -=1;
else:
    print("you lose")    



# is gussed input is in word

# 3. check if letter the user gussed is correct or not

 
stages = [
        """
            +-------+
            |
            |
            | 
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            | 
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |       |
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |      -|
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |      /
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |      / \
            |
         ==============
        """]



