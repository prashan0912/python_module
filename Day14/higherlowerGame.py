

# todo

# 1.create data table
# 2.taking input
# 3. game over

from game_data import game_data

import random 


# a = random.choice(game_data[0:5]);

# b = random.choice(game_data[6:10]);

# print("first person: ",a["name"],a["profession"] )
# print("VS")
# print("first person: ",b["name"],b["profession"] )

# input("Enter whome you choose: ")

print("game Start")
game_over = False
score = 0 
# a = random.choice(game_data[0:5]);
# print(a);

while not game_over:

    # a = random.choice(game_data[0:5]);
    # b = random.choice(game_data[5:10]);
    
    a, b = random.sample(game_data, 2)
    
    print("first person: ",a["name"],a["profession"] )
    print("VS")
    print("second person: ",b["name"],b["profession"] )
    myinput = input("Enter whome you choose:  'A' and 'B' : ").upper()

    if myinput == 'A':
        if(int(a["follower"])>int(b["follower"])):
            score += 1;
            print("score",score)
        else:
            print("Game over , Your score: ",score) 
            game_over = True;   
    elif myinput == "B":
        if(int(a["follower"])<int(b["follower"])):
            score += 1;
            print("score",score)
        else:
            print("Game over , Your score: ",score)
            game_over =True
            
            
           
            
    
