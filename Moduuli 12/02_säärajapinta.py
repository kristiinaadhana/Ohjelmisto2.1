import requests
import json

kaupunki = input("Syötä kaupungin nimi: ")

pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&units=metric&lang=FI&appid=f5a5952a2dc7a1d0d5c6ad4c9bf57cbe"
vastaus = requests.get(pyynto)

if vastaus.status_code == 200:
    data = vastaus.json()
    säänkuvaus = data['weather'][0]['description']
    lämpötila = data['main']['temp']
    print(f"Säätilan kuvaus: {säänkuvaus}")
    print(f"Lämpötila: {lämpötila}°C ")
else:
    print("Hakua ei voitu suorittaa.")


