import enemy
import player


def propCalculator(playerWin, enemyWin) -> list:
    if abs(playerWin - enemyWin) < ((playerWin + enemyWin) * 0.001):
        return [0, 0]
    
    try:
        propPlayer = ((playerWin)/(playerWin + enemyWin)) - 0.5
        propEnemy = ((enemyWin)/(playerWin + enemyWin)) - 0.5
        normPlayer = propPlayer / 0.5
        normEnemy = propEnemy / 0.5

        return [normPlayer*100, normEnemy*100]
    except:
        print("division by 0")
        return [0, 0]

    
def defineWinner(playerPoints, enemyPoints) -> str:
    if playerPoints < enemyPoints:
        print("[Arena] Enemy win")
        return "enemy"
    elif playerPoints > enemyPoints:
        print("[Arena] Player win")
        return "player"
    elif playerPoints == enemyPoints:
        print("[Arena] Tie")
        return "tie"
    

def playWinner(playerPlay:str, enemyPlay:str) -> list: # [0] - player, [1] - enemy
    if playerPlay == enemyPlay:
        return [0, 0]
    elif playerPlay == "rock" and enemyPlay == "paper":
        return [0, 1]
    elif playerPlay == "paper" and enemyPlay == "scissors":
        return [0, 1]
    elif playerPlay == "scissors" and enemyPlay == "rock":
        return [0, 1]
    else:
        return [1, 0]


def main() -> str:
    playerWins, enemyWins = 0, 0
    playerPoints, enemyPoints = 0, 0
    playerPlay , enemyPlay = "", ""

    for i in range(gameLength):
        for j in range(playLength):
            playerPlay = player.strategy.play()
            enemyPlay = enemy.strategy.play()
            player.strategy.handle_moves(playerPlay, enemyPlay)
            playPoints = playWinner(playerPlay, enemyPlay)
            playerWins += playPoints[0]
            enemyWins += playPoints[1]
        
        gameWins = propCalculator(playerWins, enemyWins)
        playerPoints = gameWins[0]
        enemyPoints = gameWins[1]
        playerWins = 0
        enemyWins = 0

    return defineWinner(playerPoints, enemyPoints)


if __name__ == "__main__":
    gameLength: int = 100
    playLength: int = 2000
    p, e, tie = 0, 0, 0
    for i in range(100):
        a = main()
        if a == "player":
            p += 1
        elif a == "enemy":
            e += 1
        elif a == "tie":
            tie += 1
    print(f"player: {p}, enemy: {e}, tie: {tie}")