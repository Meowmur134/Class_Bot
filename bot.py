import config
import telebot
import random


TOKEN = config.TOKEN
bot = telebot.TeleBot(TOKEN)
JOKES = [
    "Программист — это человек, который решает проблему, о которой вы не знали, способом, который вы не понимаете.",
    "В мире есть 10 типов людей: те, кто понимает двоичную систему, и те, кто нет.",
    "— Алло, это техподдержка? У меня интернет не работает. — А какой у вас браузер? — Синий такой, с буквой Е."
]


class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def info(self):
        return f"Машина: {self.brand}, цвет: {self.color}"


# Handle '/info'
@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, """\
Информация о боте: Я простой эхо-бот. Отправь мне любое сообщение\
, и я повторю его!""")


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll\
say the exact same thing to you!""")


# Handle '/joke'
@bot.message_handler(commands=['joke'])
def send_joke(message):
    joke = random.choice(JOKES)
    bot.reply_to(message, joke)


# Handle '/car'
@bot.message_handler(commands=['car'])
def create_car(message):
    color = message.text.split()[1]
    brand = message.text.split()[2]
    car = Car(color, brand)
    bot.reply_to(message, car.info())


# Handle all other messages with content_type 'text' (content_types defaults\
# to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
