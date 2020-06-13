from src.handlers.handler import Handler
from src.keyboard import *

from locales.ru import buttons as btn_text
from locales.ru import messages as msg_text


class TextMessageHandler(Handler):
    def activate(self):
        self.add_handler(self.request_loc, func=lambda m: m.text == btn_text['close_place_btn'])
        self.add_handler(self.choose_category, func=lambda m: m.text == btn_text['obzori_btn'])
        self.add_handler(self.menu, func=lambda m: m.text == btn_text['menu_btn'])
        self.add_handler(self.send_bank, func=lambda m: m.text == btn_text['metro_btn'])
        self.add_handler(self.send_centr_stations, func=lambda m: m.text == btn_text['centr_btn'])
        self.add_handler(self.send_other_stations, func=lambda m: m.text == btn_text['rightb_btn'])

    def request_loc(self, m):
        self.bot.send_message(m.chat.id,
                         msg_text['request_loc'],
                         reply_markup=req_loc_kb)

    def choose_category(self, m):
        self.bot.send_message(m.chat.id, msg_text['choose_category'], reply_markup=category_kb)

    def menu(self, m):
        self.bot.send_message(m.chat.id, msg_text['menu'], reply_markup=start_kb)

    def send_bank(self, m):
        self.bot.send_message(m.chat.id,
                         msg_text['send_bank'],
                         reply_markup=metro_kb)

    def send_centr_stations(self, m):
        self.bot.send_message(m.chat.id, msg_text['send_centr_stations'], reply_markup=centr_stations_kb)

    def send_other_stations(self, m):
        self.bot.send_message(m.chat.id, msg_text['send_other_stations'], reply_markup=other_stations_kb)
