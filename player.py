class Probability:
    def __init__(self):
        self.name = "ProbabilityStrategy"
        self.counters = {"rock": "paper", "scissors": "rock", "paper": "scissors"}
        self.enemyPlayProbability = {"rock": 33, "paper": 33, "scissors": 33}
        self.prevPlays = [] # list[list[str]]
        self.timesPlayed = {"rock": 0, "paper": 0, "scissors": 0}
        self.probCorrectingValue = 0.1

    def play(self) -> str:
        play = self.decidePlay()
        return play
    
    def handle_moves(self, playerPlay, enemyPlay) -> None:
        self.prevPlays.append([playerPlay, enemyPlay])
        self.correctProbability(playerPlay, enemyPlay)

    def correctProbability(self, playerPlay, enemyPlay) -> None:
        self.timesPlayed[playerPlay] += 1
        self.enemyPlayProbability[enemyPlay] -= self.enemyPlayProbability.get(enemyPlay) * self.probCorrectingValue

        for prob in self.enemyPlayProbability:
            if prob == enemyPlay:
                continue
            if self.enemyPlayProbability[prob] + (self.enemyPlayProbability.get(prob) * self.probCorrectingValue) < 100:
                self.enemyPlayProbability[prob] += self.enemyPlayProbability.get(prob) * self.probCorrectingValue

    def decidePlay(self) -> str:
        play = ""
        smallest = 0
        for k in self.enemyPlayProbability:
            if play == "":
                play = k
                smallest = self.enemyPlayProbability.get(k)
            elif smallest > self.enemyPlayProbability.get(k):
                play = k
                smallest = self.enemyPlayProbability.get(k)

        return self.counters[play]

    def printProbs(self):
        print(self.enemyPlayProbability)

probability = Probability()