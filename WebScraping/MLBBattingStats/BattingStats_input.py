"""
Created on Fri Mar 30 13:28:52 2018

@author: Kari
"""
# Basic web scrapping program that allows user to pick a team and it grabs the batting statistics 

import requests
from bs4 import BeautifulSoup

       
def mlb(team):   
    
    if team == "Astros":
        return ('http://www.espn.com/mlb/team/stats/batting/_/name/hou/houston-astros')
    elif team == 'Yankees':
        return ('http://www.espn.com/mlb/team/stats/batting/_/name/nyy/new-york-yankees')
    elif team == 'Dodgers':
        return("http://www.espn.com/mlb/team/stats/batting/_/name/lad/los-angeles-dodgers")
    elif team == 'Orioles':
        return('http://www.espn.com/mlb/team/stats/batting/_/name/bal')
    elif team == 'Red Sox':
        return('http://www.espn.com/mlb/team/stats/batting/_/name/bos/boston-red-sox')
    elif team == 'Rays':
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/tb/tampa-bay-rays")
    elif team == "Blue Jays":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/tor/toronto-blue-jays")
    elif team == "Braves":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/atl/atlanta-braves")
    elif team == "Marlins":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/mia/miami-marlins")
    elif team == "Mets":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/nym/new-york-mets")
    elif team == "Phillies":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/phi/philadelphia-phillies")
    elif team == "Nationals":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/wsh/washington-nationals")
    elif team == "Twins":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/min/minnesota-twins")
    elif team == "Royals":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/kc/kansas-city-royals")
    elif team == "White Sox":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/chw/chicago-white-sox")
    elif team == "Indians":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/cle")
    elif team == "Tigers":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/det/detroit-tigers")
    elif team == "Cubs":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/chc/chicago-cubs")
    elif team == "Reds":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/cin/index")
    elif team == "Brewers":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/mil/milwaukee-brewers")
    elif team == "Pirates":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/pit/pittsburgh-pirates")
    elif team == "Cardinals":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/stl/st-louis-cardinals")
    elif team == "Angels":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/laa/los-angeles-angels")
    elif team == "Athletics":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/oak/oakland-athletics")
    elif team == "Mariners":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/sea/seattle-mariners")
    elif team == "Rangers":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/tex/texas-rangers")
    elif team == "Diamondbacks":
        return ("http://www.espn.com/mlb/team/stats/batting/_/name/ari/index")
    elif team == "Rockies":
        return("http://www.espn.com/mlb/team/stats/batting/_/name/col/colorado-rockies")
    elif team == "Padres":
        return("http://www.espn.com/mlb/team/stats/batting/_/name/sd/san-diego-padres")
    elif team == "Giants":
        return("http://www.espn.com/mlb/team/stats/batting/_/name/sf/san-francisco-giants")
 
def main(team):       

    url = mlb(team)
    
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    battingTables = soup.find('table', class_ = 'tablehead')

    for row in battingTables.find_all('tr'):
        for cell in row.find_all('td'):
            print(cell.text, "\t", end ="")
        print('\n')
        
        

# to print specific columnts change ('td') to ('td')[0:14:13] 
# to print specific row change ('tr') to ('tr')[0:9:8]
choose_team = input("Select your team and get batting stats: ")
main(choose_team)
