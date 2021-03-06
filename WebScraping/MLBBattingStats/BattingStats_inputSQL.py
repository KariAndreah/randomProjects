# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 13:28:52 2018

@author: Kari
"""

import requests
from bs4 import BeautifulSoup
import sqlite3

team = input("Select your team and get batting stats: ")
team = team.lower()
       
mlb = { "astros":'http://www.espn.com/mlb/team/stats/batting/_/name/hou/houston-astros',
       'yankees':'http://www.espn.com/mlb/team/stats/batting/_/name/nyy/new-york-yankees',
       'dodgers':"http://www.espn.com/mlb/team/_/name/lad/los-angeles-dodgers",
       'orioles':'http://www.espn.com/mlb/team/stats/batting/_/name/bal',
       'red Sox':'http://www.espn.com/mlb/team/stats/batting/_/name/bos/boston-red-sox',
       'rays':"http://www.espn.com/mlb/team/stats/batting/_/name/tb/tampa-bay-rays",
       "blue Jays":"http://www.espn.com/mlb/team/stats/batting/_/name/tor/toronto-blue-jays",
       "braves":"http://www.espn.com/mlb/team/stats/batting/_/name/atl/atlanta-braves",
       "marlins":"http://www.espn.com/mlb/team/stats/batting/_/name/mia/miami-marlins",
       "mets":"http://www.espn.com/mlb/team/stats/batting/_/name/nym/new-york-mets",
       "phillies":"http://www.espn.com/mlb/team/stats/batting/_/name/phi/philadelphia-phillies",
       "nationals":"http://www.espn.com/mlb/team/stats/batting/_/name/wsh/washington-nationals",
       "twins":"http://www.espn.com/mlb/team/stats/batting/_/name/min/minnesota-twins",
       "royals":"http://www.espn.com/mlb/team/stats/batting/_/name/kc/kansas-city-royals",
       "white Sox":"http://www.espn.com/mlb/team/stats/batting/_/name/chw/chicago-white-sox",
       "indians":"http://www.espn.com/mlb/team/stats/batting/_/name/cle",
       "tigers":"http://www.espn.com/mlb/team/stats/batting/_/name/det/detroit-tigers",
       "cubs":"http://www.espn.com/mlb/team/stats/batting/_/name/chc/chicago-cubs",
       "reds":"http://www.espn.com/mlb/team/stats/batting/_/name/cin/index",
       "brewers":"http://www.espn.com/mlb/team/stats/batting/_/name/mil/milwaukee-brewers",
       "pirates":"http://www.espn.com/mlb/team/stats/batting/_/name/pit/pittsburgh-pirates",
       "cardinals":"http://www.espn.com/mlb/team/stats/batting/_/name/stl/st-louis-cardinals",
       "angels":"http://www.espn.com/mlb/team/stats/batting/_/name/laa/los-angeles-angels",
       "athletics":"http://www.espn.com/mlb/team/stats/batting/_/name/oak/oakland-athletics",
       "mariners":"http://www.espn.com/mlb/team/stats/batting/_/name/sea/seattle-mariners",
       "rangers":"http://www.espn.com/mlb/team/stats/batting/_/name/tex/texas-rangers",
       "diamondbacks":"http://www.espn.com/mlb/team/stats/batting/_/name/ari/index",
       "roockies":"http://www.espn.com/mlb/team/stats/batting/_/name/col/colorado-rockies",
       "padres": "http://www.espn.com/mlb/team/stats/batting/_/name/sd/san-diego-padres",
       "giants":"http://www.espn.com/mlb/team/stats/batting/_/name/sf/san-francisco-giants"}
       
url = mlb[team]
    
response = requests.get(url)
   
soup = BeautifulSoup(response.content, 'html.parser')
  
battingTables = soup.find('table', class_ = 'tablehead')

table = soup.find_all('table')[0] 

table_rows = table.find_all("tr")[2:]

text_row = list()
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text for i in td]
    text_row.append(row)
            
print(text_row)

conn = sqlite3.connect('C:\\Users\\Kari\\Desktop\\Python Projects\\BattingStatistics.db')
cursor = conn.cursor()

cursor.execute('''DROP TABLE IF EXISTS team;''')

conn.commit()

cursor.execute(''' CREATE TABLE IF NOT EXISTS team (NAME, GP, AB, R,
                                     H, secondB, thirdB, HR, 
                                     RBI, TB , BB, SO,
                                     SB, BA, OBP, SLG,
                                    OPS, OWAR)''')
conn.commit()


cursor.executemany('''INSERT INTO team VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', text_row)


    
conn.commit()
cursor.close()
conn.close() 

        

# to print specific columnts change ('td') to ('td')[0:14:13] 
# to print specific row change ('tr') to ('tr')[0:9:8]
