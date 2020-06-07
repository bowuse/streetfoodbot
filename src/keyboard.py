from telebot.types import \
        ReplyKeyboardMarkup,\
        InlineKeyboardMarkup,\
        KeyboardButton,\
        InlineKeyboardButton


class Keyboard:
    def __init__(self):
        self.btns = Buttons()

    @property
    def start_kb(self):
        return 0


class Buttons:
    @property
    def menu(self):
        return 0