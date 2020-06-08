from src.handlers.handler import Handler
from src.utils import send_place

CATEGORYS = {
    'top': ('14', '22', '15', '24'),
    'burger': ('2', '3', '17', '24', '28'),
    'shaur': ('1', '8', '9', '18', '24'),
    'falafel': ('1', '2', '9', '25'),
    'hotdog': ('8', '11', '12', '22', '26'),
    'ramen': ('10', '24', '15', '21', '29', '30'),
    'vegan': ('9', '2', '25'),
    'other': ('14', '23', '20', '13', '27', '31', '32'),
    'delivery': ('27', '28', '29', '30')
}

METRO = {
    'contract': ('1', '3', '15', '29'),
    'kreshatik': ('2', '29'),
    'maidan': ('9',),
    'arsenal': ('10',),
    'vorota': ('13',),
    'teatr': ('12', '14'),
    'palac': ('24', '25'),
    'nyvki': ('8',),
    'kpi': ('18', '29'),
    'shulya': ('22',),
    'univer': ('11',),
    'obolon': ('23',),
    'lukyan': ('20',),
    'drughbi': ('17',)
}

class CallBackHandler(Handler):
    def activate(self):
        self.add_callback_query_handle(self.send_category, func=lambda call: "category" in call.data)
        self.add_callback_query_handle(self.send_metro, func=lambda call: "metro" in call.data)

    def send_category(self, call):
        category = call.data.split("_")[1]
        for id in CATEGORYS[category]:
            send_place(self.bot, call.message.chat.id, id)

    def send_metro(self, call):
        metro = call.data.split("_")[1]
        for id in METRO[metro]:
            send_place(call.message.chat.id, id)
