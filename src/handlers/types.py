from src.handlers.handler import Handler


class TypesHandler(Handler):

    def activate(self):
        self.add_handler(self.photo, content_types=['photo'])

    def photo(self, m):
        print(m.photo[0].file_id)