
import random 



get_num = random.randint(1,100)

game_over = False


level = input("enter level of game 'easy' or 'hard' : ");



gussed_num = int(input("give your number"));


game_over = False;



# while not game_over:
if level == "easy":
    for i in range(9):
        if get_num == gussed_num:
            print("Congratulation you win ")
            game_over = True
            break;
        elif i==9:
            print("you lose")
        elif get_num > gussed_num:
            print("too low")
            gussed_num = int(input("give your number"));
        elif get_num < gussed_num:
            print("to high")
            gussed_num = int(input("give your number"));
elif level=="hard":
    for i in range(4):
        if get_num == gussed_num:
            print("Answer is",get_num)
            game_over = True
            break
        elif i==4:
             print("you lose")
        elif get_num > gussed_num:
            print("too low")
            gussed_num = int(input("give your number"));
        elif get_num < gussed_num:
            print("to high")
            gussed_num = int(input("give your number"));
else:
    print("invalid input")           
    

  
  