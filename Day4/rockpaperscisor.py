

import random; 

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Example: Displaying computer's choice
# print(f"Computer chose:\n{rock}")

player = int(input("Enter your option 0:rock 1:paper 2:scissor"));
if(player==0):
    print(rock);
elif(player==1):
    print(paper);
else:
    print(scissors)
computer = random.randint(0,2)
if(computer==0):
    print(rock);
elif(computer==1):
    print(paper);
else:
    print(scissors)

     
if(computer == 0 and player == 0):
    print("draw")       
elif(computer == 1 and player == 1):
    print("draw")
elif(computer == 2 and player == 2):
    print("draw")      
if(computer == 0 and player == 1):
    print("player win")
elif(computer == 0 and player == 2):
        print("player win")
elif(computer == 1 and player == 0):
    print("lose")
elif(computer == 1 and player == 2):
    print("lose") 
elif(computer == 2 and player == 0):
    print("lose") 
elif(computer == 2 and player == 1):
    print("lose")               
   



