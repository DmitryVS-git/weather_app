import requests
import sys
from string import punctuation, whitespace

BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"


def convert_kelvin_to_celsius(kelvin):
    celsius = round(kelvin - 273.15)
    return celsius


def main():
    try:
        with open('api_key', encoding='utf-8') as file:
            API_KEY = file.read()
    except FileNotFoundError:
        print('Невозможно открыть файл')
        sys.exit()
    except:
        print('Ошибка при работе с файлом')
        sys.exit()

    while True:
        special_chars = punctuation + whitespace

        city = input("Please, enter the city: ").title().strip(special_chars)
        url = f"{BASE_URL}appid={API_KEY}&q={city}"
        response = requests.get(url).json()
        resp_code = int(response['cod'])

        if resp_code != 200:
            print('Incorrect. Please, type your city correctly')
            continue
        break

    temp_kelvin = response["list"][0]["main"]['temp']
    temp_celsius = convert_kelvin_to_celsius(temp_kelvin)
    feels_like_kelvin = response["list"][0]["main"]['feels_like']
    feels_like_celsius = convert_kelvin_to_celsius(feels_like_kelvin)
    humidity = response["list"][0]["main"]['humidity']
    description = response["list"][0]['weather'][0]['description']

    print(f'''
        City: {city}
        --------------------------------------
        temperature: {temp_celsius}℃
        feels_like: {feels_like_celsius}℃
        humidity: {humidity}%
        weather: {description}
        --------------------------------------
    ''')


if __name__ == '__main__':
    main()
