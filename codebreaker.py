import random


def generateCode():
    code = []
    for x in range(4):
        code.append(random.randrange(1,7))
    return code
    
def generateHint(guess,code):
    hint = []
    for x in range(len(code)):
        if guess[x]==code[x]:
            hint.append(2)
        else:
            try:
                ind=code.index(guess[x])
            except ValueError:
                ind=-1
            if ind !=-1:
                hint.append(1)
    hint.sort(reverse=True)
    return hint

def strToList(string):
    li= []
    for x in string:
        li.append(int(x))
    return li

def userGuess():
    cleanGuess = False
    while not cleanGuess:
        cleanGuess=True
        inp=input("Enter your guess: ")
        if len(inp)!=4:
            cleanGuess=False
        for x in inp:
            if x != "1" and x != "2" and x != "3" and x != "4" and x != "5" and x != "6":
                cleanGuess=False
        if not cleanGuess:
            print("Guess should only include 4 numbers 1 through 6")
    return strToList(inp)
    
def intro():
    print("===========================================================")
    print("Welcome to Master Mind by Artem")
    print("The secret code has been created and you have 12 turns to figgure it out. Good luck!")
    return generateCode()


def turn(scrt):
    print("Turn "+str(x+1))
    attempt = userGuess()
    if scrt !=attempt:
        print("The hint:")
        print(generateHint(attempt,scrt))
        return False
    else: 
        print("Congratulations you are correct")
        return True


again = True
while again:
    scrt=intro()
    victory= False
    for x in range(12):
        if turn(scrt):
            victory= True
            break
    if not victory:
        print("You lost! The code was:")
        print(scrt)
    responded = False
    while not responded:
        inp=input("Would you like to play again? (y/n): ")
        if inp == "y":
            responded = True
        if inp == "n":
            again = False
            responded = True



        

