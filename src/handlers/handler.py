from src.keyboard import Keyboard, Buttons

class Handler:
    def __init__(self, bot):
        self.bot = bot
        self.kb = Keyboard()
        self.btn = Buttons()

    def activate(self):
        pass

    def add_handler(self, handler, commands=None, regexp=None, func=None, content_types=None):
        handler_dict = self.bot._build_handler_dict(handler,
                                                    commands=commands,
                                                    regexp=regexp,
                                                    func=func,
                                                    content_types=content_types)
        self.bot.message_handlers.append(handler_dict)

    def add_callback_query_handle(self, handler, func, **kwargs):
        handler_dict = self.bot._build_handler_dict(handler, func=func, **kwargs)
        self.bot.callback_query_handlers.append(handler_dict)