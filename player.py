import random

class Probability:
    def __init__(self):
        self.name = "Probability"
        self.counters = {"rock": "paper", "scissors": "rock", "paper": "scissors"}
        self.enemyPlayProbability = {"rock": 0, "paper": 0, "scissors": 0}
        self.timesPlayed = {"rock": 0, "paper": 0, "scissors": 0}
        self.round = 1

    def play(self) -> str:
        play = self.decidePlay()
        return play
    
    def handle_moves(self, playerPlay, enemyPlay) -> None:
        self.correctProbability(enemyPlay)
        self.round += 1

    def correctProbability(self, enemyPlay) -> None:
        self.timesPlayed[enemyPlay] += 1

        for prob in self.enemyPlayProbability:
            self.enemyPlayProbability[prob] = self.timesPlayed[prob] / self.round

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
    
    def printProb(self):
        print(self.enemyPlayProbability)


class PatternRecognition:
    def __init__(self):
        self.name = "PatternRecognition"
        self.counters = {"rock": "paper", "scissors": "rock", "paper": "scissors"}
        self.prevRounds = [] # list[plays], plays -> list[str]
        self.patterns = [] # list[patterns], pattern -> list[str]
        self.tempPattern = [] # list[str]
        self.patternBlockMinSize = 5
        self.patternBlockSizeLimit = 15
        self.patternToExamineSize = 30
        self.currentPattern = []
        self.nextPlayCurrentPattern = 0

    def play(self) -> str:
        play = self.decidePlay()
        self.nextPlayCurrentPattern += 1
        return play


    def handle_moves(self, playerPlay, enemyPlay):
        if len(self.tempPattern) > self.patternToExamineSize:
            self.tempPattern.clear()
        
        self.tempPattern.append(enemyPlay)

        if len(self.patterns) == 3**self.patternBlockMinSize and not self.patternBlockMinSize == self.patternBlockSizeLimit:
            self.patternBlockMinSize += 1

        if len(self.tempPattern) >= 6 and not self.patternBlockMinSize == 5:
            self.tryToFindPattern()
        

    def tryToFindPattern(self):
        patternBlockSize: int = self.patternBlockMinSize
        for i in range(len(self.tempPattern) - patternBlockSize):
            patternBlock = ""
            leftOutPattern = ""
            for j in range(i, i+patternBlockSize, 1): # get pattern to examine
                patternBlock += self.tempPattern[j] + ";"

            for j in range(i): # get the rest of the list elements as a big string
                leftOutPattern += self.tempPattern[j] + ";"

            for j in range(i+patternBlockSize, len(self.tempPattern), 1):
                leftOutPattern += self.tempPattern[j] + ";"

            self.isPattern(patternBlock, leftOutPattern)

    def isPattern(self, patternBlock, leftOutPattern) -> bool:
        if leftOutPattern.find(patternBlock) != -1: # check for pattern
            tempPattern = patternBlock.split(";")
            tempPattern.remove('')
            if not self.checkIfPatternExists(tempPattern):
                self.patterns.append(tempPattern)
                return True
        return False

    def checkIfPatternExists(self, pattern:list) -> bool:
        for i in self.patterns:
            if i == pattern:
                return True
        return False

    def decidePlay(self):
        if len(self.patterns) == 0 or len(self.prevRounds) < 4:
            return random.choice(["rock", "paper", "scissors"])
        lastPlayed = self.prevRounds[len(self.prevRounds)-1][1]
        if len(self.currentPattern) == 0:
            for i in self.patterns:
                if i[0] == lastPlayed:
                    self.currentPattern = i
                    return i[1]
        else:
            return self.currentPattern[self.nextPlayCurrentPattern]

    def printPatterns(self):
        print(self.patterns)


class Random:
    def __init__(self):
        pass

    def play(self):
        return random.choice(["rock", "paper", "scissors"])

    def handle_moves(self, s, d):
        pass




strategy = Probability()