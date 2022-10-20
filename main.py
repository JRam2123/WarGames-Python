import random
import valid
name = ''
def welcome():

    print("Hello...")
    print("My name is Joshua...")
    name = str(input("What is your name?"))
    print("Hello",name)



def main():
    welcome()
    while True:
        print("Would you like to play a game,",name)
        yesNo = input()
        while (not valid.isValid(yesNo)):
            print("\nError")
            yesNo = input()

    totalJosh = 0
    totalUser = 0
    totalPlayed = 0
    totalTied = 0


main()