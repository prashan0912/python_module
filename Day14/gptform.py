import random
from game_data import game_data

print("Game Start")

game_over = False
score = 0

a = random.choice(game_data)

while not game_over:
    b = random.choice(game_data)

    # avoid same person
    while a == b:
        b = random.choice(game_data)

        print("\nFirst person:", a["name"], "-", a["profession"])
        print("VS")
        print("Second person:", b["name"], "-", b["profession"])

        myinput = input("Enter choice (A/B): ").upper()

        if myinput == 'A':
            if int(a["follower"]) > int(b["follower"]):
                score += 1
                print("Correct! Score:", score)
                a = b   # next round continues
            else:
                print("Game Over! Your score:", score)
                game_over = True

        elif myinput == 'B':
            if int(a["follower"]) < int(b["follower"]):
                score += 1
                print("Correct! Score:", score)
                a = b
            else:
                print("Game Over! Your score:", score)
                game_over = True