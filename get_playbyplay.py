import requests
from bs4 import BeautifulSoup



def playbyplay(gameID):
    res = requests.get('http://www.espn.com/nba/playbyplay?gameId=' + gameID)
    soup = BeautifulSoup(res.text, "lxml")
    wrapper = soup.find('div',{'id': 'gp-quarter-1'})
    table = wrapper.find('table').findAll('tr')
    print(table)
    return 'test'