#pip install requests and beautifulsoup libraries and import into file
import requests
from bs4 import BeautifulSoup
#pip install twilio and import Client into file
from twilio.rest import Client

#declare variables a and soup
a = requests.get("https://www.skysports.com/football-fixtures")
soup = BeautifulSoup(a.text, features="html.parser")

#create empty list labelled 'teams'. For loop using find_all function to find all elements underneath both html classes. Append into list
teams = []
for date in soup.find_all(class_="fixres__header2"):
    for i in soup.find_all(class_="swap-text--bp30")[1:]:
        teams.append(i.text)

#declare variable for date. 
date = soup.find(class_="fixres__header2").text
print(date)

#strip extra spaces
teams = [i.strip('\n') for i in teams]

#for loop for printing teams in page
for team in range(0, (len(teams)-1)):
    print(teams[team] + " vs " + teams[team+1])

#create empty list labelled 'league'. Same process repeated to find all elements with league names
league = []
for date in soup.find_all(class_="fixres_header2"):
    for i in soup.find_all(class_="fixres__header3"):
        league.append(i.text)
        
#strip extra spaces. Declare empty list labelled 'final'
league = [i.strip('\n') for i in league]
final = []

#same process as above but printing league names and team names
for x in range(0, len(teams), 5):
    final.append(teams[x] + "vs" + teams[x+1])
for i in league:
    print(i)
    for i in final:
        print(i)

#input twilio credentials from twilio account 
account_sid = "AC44610845ca05d5ab6d136e38d726bb7a"
auth_token = "34368e615e3a5770f3b35b7a9f6b7ed1"
client = Client(account_sid, auth_token)

#function for sending twilio SMS message to phone
def send_message():
    client.messages.create(
        to="xxxxxxx",
        from_="xxxxxxx",
        body=str(teams))


print(send_message())





