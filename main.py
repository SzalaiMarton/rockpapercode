import strategy
import enemy as e
import math

player = strategy.Strategies
enemy = e.Enemy

gameLength = 5
playLength = 20

def propotionCalculator(playerWins:int, enemyWins:int) -> list:
    if abs(playerWins - enemyWins) < ((playerWins + enemyWins) * 0.001):
        return [0, 0]
    
    propPlayer = (playerWins / (playerWins + enemyWins)) - 0.5
    propEnemy = (enemyWins / (playerWins + enemyWins)) - 0.5

    normalizedPlayer = propPlayer / 0.5
    normalizedEnemy = propEnemy / 0.5

    totalPlayer = normalizedPlayer * 100
    totalEnemy = normalizedEnemy * 100

    return [totalPlayer, totalEnemy]


def decideWinner(playerPoints:int, enemyPoints:int) -> str:
    playerPoints /= gameLength
    enemyPoints /= gameLength

    if playerPoints > enemyPoints:
        return "[Arena] Player wins"
    elif playerPoints < enemyPoints:
        return "[Arena] Enemy wins"
    else:
        return "[Arena] Tie"


def playWinner(playerPlay:str, enemyPlay:str) -> list: # [0]-own, [1]-enemy
    if playerPlay == enemyPlay:
        print("     [Play] Tie")
        return [0,0]
    elif playerPlay == "rock" and enemyPlay == "paper":
        print("     [Play] Enemy win")
        return [0,1]
    elif playerPlay == "paper" and enemyPlay == "scissors":
        print("     [Play] Enemy win")
        return [0,1]
    elif playerPlay == "scissors" and enemyPlay == "rock":
        print("     [Play] Enemy win")
        return [0,1]
    else:
        print("     [Play] Player win")
        return [1,0]
    

def main() -> None:
    playerWins, enemyWins = 0, 0
    playerPoints, enemyPoints = 0, 0
    playerPlay, enemyPlay = "", ""
    wins = []
    for i in range(gameLength):
        for j in range(playLength):
            playerPlay = player.play(player)
            enemyPlay = enemy.play(enemy)

            player.handle_moves(playerPlay, enemyPlay)
            
            wins = playWinner(playerPlay, enemyPlay)
            playerWins += wins[0]
            enemyWins += wins[1]
            print("")

        props = propotionCalculator(playerWins, enemyWins)
        playerPoints += props[0]
        enemyPoints += props[1]
        playerWins, enemyWins = 0, 0
    
    print(decideWinner(playerPoints,enemyPoints))

if __name__ == "__main__":
    main()