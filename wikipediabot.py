import telebot
from telebot import types
from googletrans import Translator
import wikipedia

bottoken = '6773279075:AAEINqCRNv565HmaRNSm5Y-Sw_7Q4y3xTtE'
bot = telebot.TeleBot(bottoken)
translator = Translator()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Send keyword to search in wikipedia")


@bot.message_handler(func=lambda message: True)
def search_wikipedia(message):
    try:
        search_query = message.text
        search_results = wikipedia.search(search_query)
        if search_results:
            page = wikipedia.page(search_results[0])
            summary = wikipedia.summary(search_results[0], sentences=1)
            bot.send_message(message.chat.id, f"{summary}\n\n{page.url}")
        else:
            bot.send_message(message.chat.id, "No Result")
    except Exception as e:
        print(e)

bot.polling()