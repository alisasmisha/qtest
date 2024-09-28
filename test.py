import random


number = random.randint(1, 10)
correct = False
attempts = 0

while(not correct):
    print("pick a number 1 - 10")
    userInput = input()

    if (number == int(userInput)):
        attempts += 1
        print("OMG WOW ARE U A PSYCIC, U GOT IT RIGHT")
        print("It took you ", attempts, " attempts :D")
        correct = True

    else:
        attempts += 1
        print("NOpe bitch")
        print("TRY AGAIN")
        print("Youre on ", attempts, " attempts")