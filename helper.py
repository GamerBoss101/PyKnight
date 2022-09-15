
import storage

def addPoints(amount):
    storage.points += amount 

def addScore(amount): 
    storage.score += amount

def listMoves():
    final = ""
    for move in storage.moves:
        final += ("" move + " | ")
    print(final)