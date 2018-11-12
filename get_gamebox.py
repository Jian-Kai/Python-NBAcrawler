import requests
from bs4 import BeautifulSoup

def get_wrapper(soup, team):
    wrapper = soup.find('div',{'class', 'col column-one gamepackage-'+ team +'-wrap'})
    scoretable = wrapper.find('table')

    def score_thead(head):
        index = 0
        for inner in head:
            head[index] = inner.contents[0]
            index += 1
        return head    
    
    def score_tbody(body):
        
        index = 0
        for inner in range(0, len(body)-2, 1):
            inindex = 0
            player = body[inner].findAll('td')
            for play in player:
                if(inindex == 0):
                    player[inindex] = [play.find('span',{'class','abbr'}).contents[0], play.find('span',{'class','position'}).contents[0]]
                else:                
                    player[inindex] = play.contents[0]
                inindex += 1 
            body[index] = player
            index += 1
        return body[:-2]
    
    #start player
    startthead = score_thead(scoretable.findAll('thead')[0].findAll('th'))
    startscroe = score_tbody(scoretable.findAll('tbody')[0].findAll('tr'))
    #bench player
    benchthead = score_thead(scoretable.findAll('thead')[1].findAll('th'))
    benchscroe = score_tbody(scoretable.findAll('tbody')[1].findAll('tr'))

    return [startthead, startscroe, benchthead, benchscroe]





def gamebox(gameID):
    res = requests.get('http://www.espn.com/nba/boxscore?gameId=' + gameID)
    soup = BeautifulSoup(res.text, "lxml")
    
    box = get_wrapper(soup, 'away')
    return box