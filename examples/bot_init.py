import telebot

token = '5219990394:AAGJRCUNmzZvoIxuX0nNyN1DVN-sbfY5FGM'

bot = telebot.TeleBot(token)
print(bot.get_me())
