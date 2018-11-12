import get_game
import get_gamebox

class GameBox:
    starts = ''
    bench = ''

class GameMatch:
    HomeTeam = ''
    AwayTeam = ''
    GameStatus = ''

gameinfo = get_game.get_game('401070837')
gamebox = get_gamebox.gamebox('401070837')

Game = GameMatch()
Game.AwayTeam = gameinfo[0]
Game.HomeTeam = gameinfo[1]
Game.GameStatus = gameinfo[2]

GmaeBox = GameBox()
GameBox.starts = [gamebox[0], gamebox[1]]
GameBox.bench = [gamebox[2], gamebox[3]]

