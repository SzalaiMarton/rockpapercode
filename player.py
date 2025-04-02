class Probability:
    def __init__(self):
        self.name = "Probability"
        self.counters = {"rock": "paper", "scissors": "rock", "paper": "scissors"}
        self.enemyPlayProbability = {"rock": 0, "paper": 0, "scissors": 0}
        self.timesPlayed = {"rock": 0, "paper": 0, "scissors": 0}
        self.round = 1
        self.prevRounds = []
        self.searchDepth = 20
        self.counterBot = False
        self.prevEnemyMove = ""
        self.prevPlayerMove = ""

    def play(self) -> str:
        play = self.decidePlay()
        return play
    

    def handle_moves(self, playerPlay, enemyPlay) -> None:
        self.prevEnemyMove = enemyPlay
        self.prevPlayerMove = playerPlay
        if not self.counterBot:
            self.correctProbability(enemyPlay)
        else:
            return
        self.round += 1
        self.prevRounds.append([playerPlay, enemyPlay])
        if len(self.prevRounds) == self.searchDepth:
            if self.detectCounterBot():
                self.counterBot = True
            self.prevRounds.clear()

    def correctProbability(self, enemyPlay) -> None:
        self.timesPlayed[enemyPlay] += 1

        for prob in self.enemyPlayProbability:
            self.enemyPlayProbability[prob] = self.timesPlayed[prob] / self.round

    def detectCounterBot(self) -> bool:
        notCounter, counter = 0, 0
        counterBot = 0.7    # if counter plays counts exceeds the searchDepth's 80% it is a counter bot
        for plays in self.prevRounds:
            if plays[1] == self.counters[plays[0]]:
                counter += 1
            else:
                notCounter += 1

        if counter >= self.searchDepth*counterBot:
            return True
        else:
            return False

    def decidePlay(self) -> str:
        if not self.counterBot:
            play = ""
            highest = 0
            for k in self.enemyPlayProbability:
                if play == "":
                    play = k
                    highest = self.enemyPlayProbability.get(k)
                elif highest < self.enemyPlayProbability.get(k):
                    play = k
                    highest = self.enemyPlayProbability.get(k)
        else:
            return self.counterMove(self.prevEnemyMove)


        return self.counters[play]
    
    def counterMove(self, move):
        temp = self.counters.get(move)
        if temp == self.prevPlayerMove:
            return move
        return temp
    
strategy = Probability()