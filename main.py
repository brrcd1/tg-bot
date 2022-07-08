import telebot
import requests
from telebot import types
from config import API_token

bot = telebot.TeleBot('5572757387:AAE-xNgPhJVYj-X_pP0yqnbewg1jVjLA8ZY')


@bot.message_handler(commands=['start'])
def start(message):
    name = f'<b>Йо {message.from_user.first_name}, я напомню тебе что угодно</b>'
    bot.send_message(message.chat.id, name, parse_mode='html')


@bot.message_handler(commands=['translate'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("гугл переводчик",
                                          url="https://translate.google.com/?hl=ru&sl=en&tl=ru&text=polling&op=translate"))
    bot.send_message(message.chat.id, 'если нужен переводчик', reply_markup=markup)


@bot.message_handler(commands=['weather'])
def get_weather(message):
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
            f"https://api.openweathermap.org/data/2.5/weather?q={message}&appid={API_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, я сам не понимаю, что там происходит"

        wind = data["wind"]["speed"]

        bot.send_message(message, f"Погода в городе: {city}\n Температура: {cur_weather}C° {wd}\n"
                         f"\nВетер: {wind} м/с\n"
                         f"***Хорошего дня***!"
                         )

    except:
        bot.send_message('Ошибка')


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    note = types.KeyboardButton('Заметка')
    markup.add(translate, note)


bot.polling(none_stop=True)
