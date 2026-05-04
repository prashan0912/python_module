
import random
words = ["apple","banana","orange","pineapple","kiwi"]

word = random.choice(words)

print(word)

is_gameover = False

display = ["_"]*len(word)
live = 6
chache = []


while not is_gameover: 
    print(display)
    
    if(live<0):
        print("Game Over")
        is_gameover = True
        exit()
    
    guess = input("enter your input char here : ").lower()
    
    for j in chache:
        if j==guess:
            print("already text")
        else:
            chache.append(guess)
    print(chache)    
    found = False;        
    for index,char in enumerate(word):
        if char == guess:
            display[index] = guess
            found = True
            
            
    if not found:
        print("lose one live")
        live -= 1
        
    if "_" not in display :
        print("you win")
        is_gameover = True    
                 
                    
            
# while is_gameover:
# print(display, live)