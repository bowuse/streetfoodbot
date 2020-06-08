from src.handlers.handler import Handler
from src.utils import find_closest, send_place

class TypesHandler(Handler):

    def activate(self):
        self.add_handler(self.photo, content_types=['photo'])
        self.add_handler(self.location, content_types=['location'])

    def photo(self, m):
        print(m.photo[0].file_id)

    def location(self, m):
        lat_user = m.location.latitude
        long_user = m.location.longitude
        ids = find_closest(lat_user, long_user, 5)
        for place_id in ids:
            send_place(self.bot, m.chat.id, place_id)
