import requests
from twilio.rest import Client

api_key = "39ee03e9229e88751b2073d0974f3adb"
account_sid="AC79ce10d07876dfa4b7387566fc44d01d"
auth_token="b216009bc219a23ecbcecaf329455158"



params={
    "lat":54.356030,
    "lon":18.646120,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall",params=params)
response.raise_for_status()


data = response.json()

flag = False

for key in range(0,12):
    if data["hourly"][key]["weather"][0]["id"]<700:
        flag=True

if(flag):
    client=Client(account_sid,auth_token)
    message=client.messages.create(
        body="It's raining",
        from_="+17655713977",
        to="+48698765106"
    )
    
