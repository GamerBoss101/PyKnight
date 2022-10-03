
import storage

def vaildate(prompt, args1, args2): 
    something = input(prompt + "\n" + args1 + "/" + args2 + ": ")
    while something != args1 and something != args2:
        print("Use a vaild answer choice.")    
        something = input(prompt + "\n" + args1 + "/" + args2 + " ")
    return something

def addPoints(amount):
    storage.points += amount 

def addScore(amount): 
    storage.score += amount

def listMoves():
    final = ""
    for move in storage.moves:
        final += ("" + move + " | ")
    print(final)