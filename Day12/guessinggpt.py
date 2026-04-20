import random

get_num = random.randint(1, 100)

level = input("Enter level of game 'easy' or 'hard': ")

if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    print("Invalid input")
    exit()

for i in range(attempts):
    guessed_num = int(input("Give your number: "))

    if guessed_num == get_num:
        print("🎉 Congratulations, you win!")
        break
    elif guessed_num < get_num:
        print("Too low")
    else:
        print("Too high")

        print(f"Attempts left: {attempts - i - 1}")
else:
    print("😢 You lose")
    print("The number was:", get_num)