import requests
from bs4 import BeautifulSoup

def CapturePlay(table):
    Play = []
    for index in range(1, len(table)):
        details = table[index].findAll('td')
        temp = []
        for detail in details:
            if detail.contents:
                temp.append(detail.contents[0])   
        Play.append(temp)

    return  Play


def playbyplay(gameID):
    res = requests.get('http://www.espn.com/nba/playbyplay?gameId=' + gameID)
    soup = BeautifulSoup(res.text, "lxml")
    wrapper = soup.find('div',{'id': 'gp-quarter-1'})
    table = wrapper.find('table').findAll('tr')
    CapturePlay(table)
    #print(table)
    return 'test'