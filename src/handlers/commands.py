from src.handlers.handler import Handler

class CommandHandler(Handler):
    def activate(self):
        self.add_handler(self.help, commands=['help'])
        self.add_handler(self.start, commands=['start'])

    # /help
    def help(self, m):
        self.bot.send_message(m.chat.id, 'Hello, its help message')

    # /start
    def start(self, m):
        self.bot.send_message(m.chat.id, 'Glad to see you, old friend')
