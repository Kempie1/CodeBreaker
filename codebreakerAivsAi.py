import random


#
#
#
#
#
#           Bug in generateHint
#           I think possibleGuesses() should work if generateHint works as expected
#
#
#
#
#
#
#
#

def generateCode():
    code = []
    for x in range(4):
        code.append(random.randrange(1,7))
    return code
    
def generateHint(guess,code):
    hint1locations=[]
    hint1=0
    hint2=0

    for x in range(len(code)):
        if guess[x]==code[x]:
            hint1+=1
            hint1locations.append(x)
    for x in range(len(code)):
        occurance=[]
        for i in range(len(code)):
            if code[i] == guess[x]:
                occurance.append(i)
        for x in occurance:
            for y in hint1locations:
                if y != x:
                    hint2+=1
    return [hint1,hint2]
        


def generateGuesses():
    guesses=[]
    for w in range (1,7):
        for x in range(1,7):
            for y in range (1,7):
                for z in range(1,7):
                    guesses.append([z,y,x,w])
    return guesses



def possibleGuesses(hint, lastguess, guesses):
    wrongGuesses=[]
    for x in guesses:
        if generateHint(x,lastguess) != hint:
            wrongGuesses.append(x)
    for x in range(len(wrongGuesses)):
        guesses.remove(wrongGuesses[x])
    print(guesses)
    return guesses


def logic():
    if len(availableGuesses) >1:
        currentGuess=random.randrange(0,(len(availableGuesses)-1))
        return availableGuesses[currentGuess]
    return availableGuesses[0]


def strToList(string):
    li= []
    for x in string:
        li.append(int(x))
    return li

    
def intro():
    print("===========================================================")
    print("Welcome to Master Mind by Artem")
    print("The secret code has been created and you have 12 turns to figgure it out. Good luck!")
    return generateCode()


def turn(scrt):
    
    input("Press Enter to continue")
    print("-----------------------------------------------------------")
    print("Turn "+str(x+1))
    attempt = logic()
    print("The computer guessed:")
    print(attempt)
    if scrt !=attempt:
        print("The hints:")
        hint=generateHint(attempt,scrt)
        print("Hint 1:" +str(hint[0]))
        print("Hint 2:" +str(hint[1]))
        global availableGuesses
        availableGuesses = possibleGuesses(hint,attempt,availableGuesses)
        return False
    else: 
        print("Congratulations you are correct")
        return True


availableGuesses= generateGuesses()
again = True
while again:
    scrt=intro()
    print(scrt)
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



        

