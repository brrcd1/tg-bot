import requests
from pprint import pprint
from config import API_token

def get_weather(city, API_token):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_token}&units=metric"
        )
        data = r.json()
        pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, я сам не понимаю, что там происходит"

        wind = data["wind"]["speed"]
        print(f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
              f"\nВетер: {wind} м/с\n"
              f"Хорошего дня!"
              )

    except Exception as ex:
        print(ex)
        print('Ошибка')


def main():
    city = input('Введите город: ')
    get_weather(city, API_token)


if __name__ == '__main__':
    main()
