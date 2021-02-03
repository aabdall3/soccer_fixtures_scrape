import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

a = requests.get("https://www.skysports.com/football-fixtures")
soup = BeautifulSoup(a.text, features="html.parser")

teams = []
for date in soup.find_all(class_="fixres__header2"):
    for i in soup.find_all(class_="swap-text--bp30")[1:]:
        teams.append(i.text)

date = soup.find(class_="fixres__header2").text
print(date)
teams = [i.strip('\n') for i in teams]

for team in range(0, (len(teams)-1)):
    print(teams[team] + " vs " + teams[team+1])

league = []
for date in soup.find_all(class_="fixres_header2"):
    for i in soup.find_all(class_="fixres__header3"):
        league.append(i.text)
league = [i.strip('\n') for i in league]
final = []

for x in range(0, len(teams), 5):
    final.append(teams[x] + "vs" + teams[x+1])
for i in league:
    print(i)
    for i in final:
        print(i)

account_sid = "AC44610845ca05d5ab6d136e38d726bb7a"
auth_token = "34368e615e3a5770f3b35b7a9f6b7ed1"
client = Client(account_sid, auth_token)


def send_message():
    client.messages.create(
        to="xxxxxxx",
        from_="xxxxxxx",
        body=str(teams))


print(send_message())





