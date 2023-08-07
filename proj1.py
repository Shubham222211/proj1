import requests
import json

apikey = "baaf4d62b58a6a2a15578a957bc00715"
baseurl = "https://api.openweathermap.org/data/2.5/weather?q="
cityname = input("Enter the city name: ")
completeurl = baseurl + cityname + "&appid=" + apikey
response = requests.get(completeurl)
data = response.json()
kelvin=data["main"]["temp"]
final=kelvin-273.15
print("Current Temperature of your city is",final,"°C")

