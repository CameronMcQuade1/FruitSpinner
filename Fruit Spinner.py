import random
import time
fruits = ("Bar", "Lemon", "777", "Cherry", "Blueberry", "Watermelon")
chips = 100

while chips > 0:
    print("You have", chips, "chips, do you want to spin? y / n")
    spin = input()
    if spin == "n":
        print("Goodbye!")
        quit()
    elif spin == "y":
        print("How many chips do you want to bet?")
        try:
            bet = int(input())
        except ValueError:
            print("Numbers only!")
            continue
        if bet > chips:
            print("Not enough chips!")
            time.sleep(0.5)
            continue
        elif bet < 10:
            print("Minimum 10 chips!")
            time.sleep(0.5)
            continue
        chips = chips - bet
        time.sleep(0.5)
        print("You have", chips, "chips left")
        turn1 = random.randint(0,5)
        turn2 = random.randint(0,5)
        turn3 = random.randint(0,5)
        time.sleep(1)
        print(".....spinning.....")
        time.sleep(2)
        print(fruits[turn1],  "|", fruits[turn2], "|", fruits[turn3])
        time.sleep(1)
        if turn1 == turn2 and turn1 == turn3:
            win = bet * 5
            chips = chips + win
            time.sleep(0.5)
            print("ALL 3! YOU WON", win, "chips")
            time.sleep(1)
            continue
        elif turn1 == turn2 or turn1 == turn3 or turn2 == turn3:
            win = bet * 2
            chips = chips + win
            time.sleep(0.5)
            print("2 numbers! you win", win, "chips")
            time.sleep(1)
    else:
        print("Invalid input!")
        continue