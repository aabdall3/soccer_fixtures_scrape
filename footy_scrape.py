#pip install requests and beautifulsoup libraries and import into file
import requests
from bs4 import BeautifulSoup

#declare variables url and page
url = "https://www.skysports.com/football-fixtures"
page = requests.get(url)

results = BeautifulSoup(page.content, "html.parser")

#declare 4 variables needed for fixtures using results variable and 'find_all' method for bs4
home = results.find_all('span', {"class": "matches__item-col matches__participant matches__participant--side1"})
dates = results.find_all('span', {"class": "matches__date"})
away = results.find_all('span', {"class": "matches__item-col matches__participant matches__participant--side2"})
comps = [team.find_previous('h5', {"class": "fixres__header3"}) for team in home]

#combine variables into zip function for simultaneous processing. Strip results to only text
for match in zip(comps, home, dates, away):
    comp, home, dates, away = [tag.text.strip() for tag in match]
    print(([tag.text.strip() for tag in match]))
