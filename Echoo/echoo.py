# import logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)

import os
import argparse
import codecs
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def escape_fn(s):
    return s.replace("_", "\\_") \
            .replace("*", "\\*") \
            .replace("[", "\\[") \
            .replace("`", "\\`") \
            .replace("<", "\\<") \
            .replace(">", "\\>")

class Echoo:
    def __init__(self, token=None, chat_id=None, parse_mode="MarkdownV2"):
        print("Init from __init__")
        self.token = token
        if token is None:
            try:
                self.token = os.environ["TG_TOKEN"]
            except KeyError:
                raise KeyError("Neither --token nor TG_TOKEN is set.")
        
        self.chat_id = chat_id
        if chat_id is None:
            try:
                self.chat_id = os.environ["TG_CHAT_ID"]
            except KeyError:
                raise KeyError("Neither --chat_id nor TG_CHAT_ID is set.")
        self.bot = telegram.Bot(token=self.token)
        # self.parse_mode = "Markdown"
        self.parse_mode = parse_mode
    
    def send_msg(self, msg, chat_id=None):
        if chat_id is None:
            chat_id = self.chat_id
        print(f"===== Echo: {msg} =====")
        self.bot.send_message(chat_id=chat_id, text=msg, parse_mode=self.parse_mode)    
    
    def __call__(self, function):
        print("Init from __call__")
        def wrapper( *args, **kwds):
            self.send_msg(escape_fn(f'''Start {str(function)}'''))
            res = function(*args, **kwds)
            self.send_msg(escape_fn(f'''Finish {str(function)}'''))
            return res
        return wrapper

def main(token, chat_id, msg="Are u ok", parse_mode="MarkdownV2"):
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=chat_id, text=escape_fn(msg), parse_mode=parse_mode)

def run():
    parser = argparse.ArgumentParser(description=r'''Echoo: A tool let's your program echo to Telegram.''')

    parser.add_argument("-t", "--token", default=None, type=str, help="Token for your bot.")
    parser.add_argument("-id", "--chat_id", default=None, type=str, help="Chat_id of your audience.")
    parser.add_argument("--parse-mode", default="Markdown", type=str, help='''Send Markdown or HTML, if you want Telegram apps to show bold,
                italic, fixed-width text or inline URLs in your bot's message''')
    parser.add_argument("msg", default="Are u ok?", type=str, help="Message to send")

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

    main(token=args.token, chat_id=args.chat_id, msg=args.msg, parse_mode=args.parse_mode)


if __name__ == '__main__':
    run()
