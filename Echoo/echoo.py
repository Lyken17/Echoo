# import logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)

import os
import argparse

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def main(token, chat_id, msg):
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=chat_id, text=msg)


def run():
    parser = argparse.ArgumentParser(description=r'''Echoo:: A tool let's your program echo.''')

    parser.add_argument("-t", "--token", default=None, type=str, help="Token for your bot.")
    parser.add_argument("-id", "--chat_id", default=None, type=str, help="Chat_id of your audience.")
    parser.add_argument("-m","--msg", default="Are u ok?", type=str, help="Message to send")

    args = parser.parse_args()
    if args.token is None:
        try:
            args.token = os.environ["TG_TOKEN"]
        except KeyError:
            raise KeyError("Neither --token nor TG_TOKEN is set.")

    if args.chat_id is None:
        try:
            args.chat_id = os.environ["TG_CHAT_ID"]
        except KeyError:
            raise KeyError("Neither --chat_id nor TG_CHAT_ID is set.")

    main(token=args.token, chat_id=args.chat_id, msg=args.msg)


if __name__ == '__main__':
    run()
