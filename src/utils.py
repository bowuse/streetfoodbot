import src.dbworker as dbw
from time import sleep
from math import radians, cos, sin, asin, sqrt

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def send_place(bot, chat_id, place_id):
    mk = InlineKeyboardMarkup()
    article_btn = InlineKeyboardButton(text='🕵 Обзор', url=dbw.get_obzor_link(place_id))
    mk.add(article_btn)

    map_link = dbw.get_map_link(place_id)
    for i in range(len(map_link)):
        addr = dbw.get_address(place_id)[i]
        mk.add(InlineKeyboardButton(text=f'🗺 {addr}', url=map_link[i]))
    bot.send_photo(
        chat_id=chat_id,
        photo=dbw.get_img_link(place_id),
        caption=format_article(
            dbw.get_name(place_id),
            dbw.get_tag(place_id),
            dbw.get_price_tag(place_id),
            dbw.get_address(place_id),
            dbw.get_descr(place_id),
            dbw.get_mark(place_id)),
        parse_mode='HTML',
        reply_markup=mk
    )
    sleep(0.5)


def format_article(name, tag, price_tag, address, descr, mark):
    if len(address) > 1:
        address = '\n'.join(address)
        address = f"\n{address}"
    else:
        address = '\n'.join(address)
    if descr:
        result = f"<b>Название: </b>{name}\n<b>Что:</b> {tag}\n<b>Цена:</b> {price_tag}\n<b>Адрес: </b>{address}\n{descr}\n<b>Оценка:</b> {mark}"
    else:
        result = f"<b>Название: </b>{name}\n<b>Что:</b> {tag}\n<b>Цена:</b> {price_tag}\n<b>Адрес: </b>{address}\n<b>Оценка:</b> {mark}"
    return result


def haversine(lat1, lon1, lat2, lon2):
    """
    Вычисляет расстояние в километрах между двумя точками, учитывая окружность Земли.
    https://en.wikipedia.org/wiki/Haversine_formula
    """

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, (lon1, lat1, lon2, lat2))

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km


def find_closest(lat_user, long_user, num) -> set:
    distances = {}
    for i in range(1, 30):
        lat = dbw.get_lat(i)
        long = dbw.get_long(i)
        distances[i] = []
        for j in range(len(lat)):
            distances[i].append(haversine(lat[j], long[j], lat_user, long_user))
    d_list = []
    for i in distances.keys():
        for j in distances[i]:
            d_list.append(j)

    # new block
    min_keys = set()
    while len(min_keys) < num:
        min_distance = min(d_list)
        d_list.remove(min_distance)
        for i in distances.keys():
            for j in range(len(distances[i])):
                if distances[i][j] == min_distance:
                    min_keys.add(i)
    return min_keys
