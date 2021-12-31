import requests
import bs4
from twilio.rest import Client

def rain_check():

    url = 'https://weather.com/en-CA/weather/today/l/06f15b4c4c753d8f49befaca8533d477bf25b5712be80fcf7a08c45d719902ef'
    rain = False

    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        weather_elem = soup.select('.today_nowcard-phrase')
        if 'rain' in weather_elem[0].text.lower():
            rain = True

    except Exception as exc:
        print(exc)
    return rain

def send_reminder(accountSID, authToken, myTwilioNumber, myCellPhone):
    twilioCli = Client(accountSID, authToken)
    message = twilioCli.messages.\
    create(body='Rain Alert! Water is (not) wet. Grab an Umbrella bro.',\
           from_=myTwilioNumber, to=myCellPhone)

if rain_check():
    send_reminder('***************', '**************', '+91********', '+91**********')
