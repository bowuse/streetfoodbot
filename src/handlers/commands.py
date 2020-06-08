from src.handlers.handler import Handler
from src.keyboard import start_kb
import src.dbworker as dbw


class CommandHandler(Handler):
    def activate(self):
        self.add_handler(self.help, commands=['help', 'start'])

    def help(self, m):
        self.bot.send_message(m.chat.id,
                         "Я бот-агрегатор обзоров от канала @streeteda. Я помогу тебе с выбором заведения 🙃",
                         reply_markup=start_kb)
        dbw.add_user(m.chat.id, m.from_user.username)

