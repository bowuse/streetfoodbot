import telebot
from env import TOKEN
from src.handlers.commands import CommandHandler
from src.handlers.types import TypesHandler
from src.handlers.text import TextMessageHandler
from src.handlers.calls import CallBackHandler

bot = telebot.TeleBot(TOKEN)

CommandHandler(bot).activate()
TypesHandler(bot).activate()
TextMessageHandler(bot).activate()
CallBackHandler(bot).activate()

if __name__ == '__main__':
	print('Bot is started & running')
	print(bot.get_me())
	bot.polling()