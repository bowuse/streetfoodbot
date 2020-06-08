from telebot.types import \
        ReplyKeyboardMarkup,\
        InlineKeyboardMarkup,\
        KeyboardButton,\
        InlineKeyboardButton

from locales.ru import buttons as btn_text


start_kb = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
close_place_btn = KeyboardButton(btn_text['close_place_btn'])
obzori_btn = KeyboardButton(btn_text['obzori_btn'])
metro_btn = KeyboardButton(btn_text['metro_btn'])
start_kb.add(close_place_btn, obzori_btn, metro_btn)

menu_btn = KeyboardButton(btn_text['menu_btn'])

req_loc_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
req_loc_btn = KeyboardButton(btn_text['req_loc_btn'], request_location=True)
req_loc_kb.add(req_loc_btn, menu_btn)

metro_kb = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
centr_btn = KeyboardButton(btn_text['centr_btn'])
rightb_btn = KeyboardButton(btn_text['rightb_btn'])
metro_kb.add(centr_btn, rightb_btn, menu_btn)

category_kb = InlineKeyboardMarkup(row_width=2)
ctop_btn = InlineKeyboardButton(btn_text['ctop_btn'], callback_data="category_top")
cburger_btn = InlineKeyboardButton(btn_text['cburger_btn'], callback_data="category_burger")
cshaur_btn = InlineKeyboardButton(btn_text['cshaur_btn'], callback_data="category_shaur")
cfalafel_btn = InlineKeyboardButton(btn_text['cfalafel_btn'], callback_data="category_falafel")
chotdog_btn = InlineKeyboardButton(btn_text['chotdog_btn'], callback_data="category_hotdog")
cramen_btn = InlineKeyboardButton(btn_text['cramen_btn'], callback_data="category_ramen")
cvegan_btn = InlineKeyboardButton(btn_text['cvegan_btn'], callback_data="category_vegan")
cother_btn = InlineKeyboardButton(btn_text['cother_btn'], callback_data="category_other")
cdeliv_btn = InlineKeyboardButton(btn_text['cdeliv_btn'], callback_data="category_delivery")
category_kb.row(ctop_btn)
category_kb.add(cburger_btn, cshaur_btn, cfalafel_btn, chotdog_btn, cramen_btn, cvegan_btn)
category_kb.row(cother_btn)
category_kb.row(cdeliv_btn)

centr_stations_kb = InlineKeyboardMarkup(row_width=1)
contract_btn = InlineKeyboardButton(btn_text['contract_btn'], callback_data="metro_contract")
kreshatik_btn = InlineKeyboardButton(btn_text['kreshatik_btn'], callback_data="metro_kreshatik")
maidan_btn = InlineKeyboardButton(btn_text['maidan_btn'], callback_data="metro_maidan")
arsenal_btn = InlineKeyboardButton(btn_text['arsenal_btn'], callback_data="metro_arsenal")
vorota_btn = InlineKeyboardButton(btn_text['vorota_btn'], callback_data="metro_vorota")
palac_btn = InlineKeyboardButton(btn_text['palac_btn'], callback_data="metro_palac")
centr_stations_kb.add(contract_btn, kreshatik_btn, maidan_btn, arsenal_btn, vorota_btn, palac_btn)

other_stations_kb = InlineKeyboardMarkup(row_width=1)
nyvki_btn = InlineKeyboardButton(btn_text['nyvki_btn'], callback_data="metro_nyvki")
kpi_btn = InlineKeyboardButton(btn_text['kpi_btn'], callback_data="metro_kpi")
shulya_btn = InlineKeyboardButton(btn_text['shulya_btn'], callback_data="metro_shulya")
univer_btn = InlineKeyboardButton(btn_text['univer_btn'], callback_data="metro_univer")
obolon_btn = InlineKeyboardButton(btn_text['obolon_btn'], callback_data="metro_obolon")
lukyan_btn = InlineKeyboardButton(btn_text['lukyan_btn'], callback_data="metro_lukyan")
drughbi_btn = InlineKeyboardButton(btn_text['drughbi_btn'], callback_data="metro_drughbi")
other_stations_kb.add(nyvki_btn, kpi_btn, shulya_btn, univer_btn, obolon_btn, lukyan_btn, drughbi_btn)
