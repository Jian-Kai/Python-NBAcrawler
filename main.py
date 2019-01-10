import get_game
import get_gamebox
import get_playbyplay
import json

class GameBox:
    starts = ''
    bench = ''

class GameMatch:
    HomeTeam = ''
    AwayTeam = ''
    GameStatus = ''

gameID = '401071198'
gameinfo = get_game.get_game(gameID)
gamebox = get_gamebox.gamebox(gameID)
gameplaybyplay = get_playbyplay.playbyplay(gameID, (len(gameinfo[2][0])-2))


#game scroe
Game = GameMatch()
Game.AwayTeam = gameinfo[0]
Game.HomeTeam = gameinfo[1]
Game.GameStatus = gameinfo[2]

#game box
GmaeBox = GameBox()
GameBox.starts = [gamebox[0], gamebox[1]]
GameBox.bench = [gamebox[2], gamebox[3]]

#save data
Gamescorejson = {}
Gamescorejson['AwayTeam'] = Game.AwayTeam
Gamescorejson['HomeTeam'] = Game.HomeTeam
Gamescorejson['GameStatus'] = Game.GameStatus
with open('data.json', 'w') as outfile:  
    json.dump(Gamescorejson, outfile)

print(len(gameplaybyplay))