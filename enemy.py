import random

class Enemy:
    def __init__(self):
        self.moves = ["rock", "paper", "scissors"]

    def play(self):
        return random.choice(self.moves)
    
en = Enemy()