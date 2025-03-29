import random

class Enemy:
    moves = ["rock", "paper", "scissors"]
    def play(self) -> str:
        return random.choice(self.moves)