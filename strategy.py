import random

class Strategies:
    def __init__(self):
        self.name: str = "RandomStrategy"
        self.prevMoves: list = [] # list[str] list -> contains all the moves that have been played
        self.moves: list = ["rock", "paper", "scissors"]

        self.counter: dict = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
        self.playProbability: dict = {"rock": 33, "paper": 33, "scissors": 33}
        self.enemyPlayProbability: dict = {"rock": 33, "paper": 33, "scissors": 33}
        self.enemyPlayCounter: dict = {"rock": 0, "paper": 0, "scissors": 0}

        self.playerProbabilityChange = 0.05;
        self.enemyProbabilityChange = 0.05;


    def play(self) -> str:
        

        play = ""        
        return play


    def handle_moves(self, ownMove: str, opponentMove: str,) -> None:
        self.prevMoves.append([ownMove, opponentMove])


    def collectingInfo(self):
        self.probabilityCorrection()


    def probabilityCorrection(self) -> None: # called when a play's probability needs to be changed
        # lower probability of recent play
        playerMove = self.prevMoves[self.prevMoves.length-1][0]
        self.playProbability[playerMove] *=  self.playerProbabilityChange
        enemyMove = self.prevMoves[self.prevMoves.length-1][1]
        self.enemyPlayProbability[enemyMove] *= self.enemyProbabilityChange

        # increase the other play's probability
        for element in self.playProbability:
            if element == playerMove:
                continue
            self.playProbability[element] += self.playProbability.get(element) * self.playerProbabilityChange
        for element in self.enemyPlayProbability:
            if element == enemyMove:
                continue
            self.enemyPlayProbability[element] += self.enemyPlayProbability.get(element) * self.enemyProbabilityChange