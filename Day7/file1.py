


import random
words = ["apple","banana","orange","pineapple","kiwi"]

word = random.choice(words)

print(word)

is_gameover = False

guess = input("enter your input char here")

myword = ["_"]*len(word)
live = 6
chache = []


print(myword)
while is_gameover: 
    if(live>0):
        print("Game Over")
        is_gameover = True
    
    guess = input("enter your input char here").lower()
    
    for j in chache:
        print("already text")
    else:
        chache.append(guess)
            
    for i in myword:
        if i == guess:
            myword = guess
            live -= 1
            
            



            

# while is_gameover:
print(myword)