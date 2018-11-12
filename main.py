import get_game
import get_gamebox
class GameMatch:
    HomeTeam = ''
    AwayTeam = ''
    GameStatus = ''

gameinfo = get_game.get_game('401070837')
Game = GameMatch()
Game.AwayTeam = gameinfo[0]
Game.HomeTeam = gameinfo[1]
Game.GameStatus = gameinfo[2]

get_gamebox.gamebox('401070837')