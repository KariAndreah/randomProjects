"""
Created on Fri Mar 30 13:28:52 2018

@author: Kari
"""

import requests
from bs4 import BeautifulSoup 

url = 'http://www.espn.com/mlb/team/stats/batting/_/name/hou/houston-astros'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

battingTables = soup.find('table', class_ = 'tablehead')

for row in battingTables.find_all('tr'):
    for cell in row.find_all('td'):
        print(cell.text, "\t", end ="")
    print('\n')

# to print specific columnts change ('td') to ('td')[0:14:13]
