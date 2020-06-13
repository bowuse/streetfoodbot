import os
import sys
sys.path.append(os.getcwd())

import telebot
from env import TOKEN, HOST_IP
from src.handlers.commands import CommandHandler
from src.handlers.types import TypesHandler
from src.handlers.text import TextMessageHandler
from src.handlers.calls import CallBackHandler

import logging
import ssl

from aiohttp import web


WEBHOOK_HOST = HOST_IP
WEBHOOK_PORT = 443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '0.0.0.0'  # In some VPS you may need to put here the IP addr

WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Path to the ssl private key

WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(TOKEN)

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(TOKEN)

CommandHandler(bot).activate()
TypesHandler(bot).activate()
TextMessageHandler(bot).activate()
CallBackHandler(bot).activate()


# Process webhook calls
async def handle(request):
    if request.match_info.get('token') == bot.token:
        request_body_dict = await request.json()
        update = telebot.types.Update.de_json(request_body_dict)
        bot.process_new_updates([update])
        return web.Response()
    else:
        return web.Response(status=403)



def build_app():
    app = web.Application()
    app.router.add_post('/{token}/', handle)
    return app

def build_ssl_context():
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV)
    return context

if __name__ == '__main__':
    print('Bot is started & running')
    print(bot.get_me())

    # Remove previous webhook
    bot.remove_webhook()

    # Set webhook
    bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                    certificate=open(WEBHOOK_SSL_CERT, 'r'))

    app = build_app()
    context = build_ssl_context()

    # Start aiohttp server
    web.run_app(
        app,
        host=WEBHOOK_LISTEN,
        port=WEBHOOK_PORT,
        ssl_context=context
    )
