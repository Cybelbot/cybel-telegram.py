import telebot

from src.utils import token, logger, _fetch

bot = telebot.TeleBot(token)

bot_data = bot.get_me()
logger.info('{} is Online'.format(bot_data.first_name))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hi! {}'.format(message.from_user.first_name))


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Help!')


@bot.message_handler(commands=['weather'])
def send_weather(message):
    bot.reply_to(message, 'Weather!')


@bot.message_handler(commands=['joke'])
def get_joke(message):
    joke_url = 'https://api.chucknorris.io/jokes/random'
    joke = _fetch(joke_url)
    bot.reply_to(message, joke['value'])


@bot.message_handler(commands=['cat'])
def get_cat(message):
    cat_url = 'https://api.thecatapi.com/v1/images/search'
    cat = _fetch(cat_url)
    bot.reply_to(message, cat[0]['url'])


@bot.message_handler(commands=['dog'])
def get_dog(message):
    dog_url = 'https://dog.ceo/api/breeds/image/random'
    dog = _fetch(dog_url)
    bot.reply_to(message, dog['message'])


@bot.message_handler(commands=['fox'])
def get_fox(message):
    fox_url = 'https://randomfox.ca/floof/'
    fox = _fetch(fox_url)
    bot.reply_to(message, fox['image'])


bot.infinity_polling()