# black jack Game

# create a card first
# take user 1 take input
# user 2 take input
# addition
# select random value
# and another

import random

cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10];


def deal_card():
    card = random.choice(cards)
    print(card)
    return card

user_cards = []
computer_cards = []


for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calculate_score(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11);
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "lose , opponent has BlackJack"
    elif user_score == 0:
        return "win with a blackjack"
    elif user_score >21:
        return "you went over . you lose"
    elif computer_score >21:
        return "opponent wnent over . you win "
    elif user_score >computer_score:
        return "You Win"
    else:
        return "you lose "
        
user_cards = []
computer_cards =[]
is_game_over = False   
computer_score = -1 

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card)    



while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards:{user_cards},current score :{user_score}")
    print(f"Computer's first card :{computer_cards[0]}")


    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        input("type Y to get another card, type 'n' to pass: ")
        if user_should_deal = "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True
        

while computer_score != 0 and computer_score <17:
    computer_cards.append(deal_card())
    computer_score =  calculate_score(computer_cards)



print(compare(user_score , computer_score ))    