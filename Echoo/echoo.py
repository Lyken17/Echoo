# import logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)

import os
import argparse
import codecs
import telegram
import asyncio
from telegram import LinkPreviewOptions
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import warnings

def escape_fn(s):
    return s.replace("_", r"\_") \
            .replace("-", r"\-") \
            .replace(".", r"\.") \
            .replace("#", r"\#") \
            .replace("*", r"\*") \
            .replace("[", r"\[") \
            .replace("`", r"\`") \
            .replace("<", r"\<") \
            .replace(">", r"\>")

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
    
    async def _send_msg(self, msg, chat_id=None, parse_mode=None):
        if chat_id is None:
            chat_id = self.chat_id
        print(f"===== Echo: {msg} =====")
        return await self.bot.send_message(chat_id=chat_id, text=msg, parse_mode=parse_mode if parse_mode else self.parse_mode, 
                                           link_preview_options=LinkPreviewOptions(is_disabled=True)
                            )
    
    def send_msg(self, msg, chat_id=None, parse_mode=None):
        return asyncio.run(
            self._send_msg(chat_id=chat_id, msg=msg, parse_mode=parse_mode if parse_mode else self.parse_mode)
        )
    
    def __call__(self, function):
        print("Init from __call__")
        def wrapper( *args, **kwds):
            self.send_msg(escape_fn(f'''Start {str(function)}'''))
            res = function(*args, **kwds)
            self.send_msg(escape_fn(f'''Finish {str(function)}'''))
            return res
        return wrapper

def main(msg="hello world", token=None, chat_id=None, parse_mode="MarkdownV2", no_escape=False, reply_to_message_id=None):
    if token is None:
        try:
            token = os.environ["TG_TOKEN"]
        except KeyError:
            raise KeyError("Neither --token nor TG_TOKEN is set.")

    if chat_id is None:
        try:
            chat_id = os.environ["TG_CHAT_ID"]
        except KeyError:
            raise KeyError("Neither --chat_id nor TG_CHAT_ID is set.")
    
    bot = telegram.Bot(token=token)
    msg_info = asyncio.run(
        bot.send_message(chat_id=chat_id, text=msg if no_escape else escape_fn(msg), 
                         parse_mode=parse_mode, reply_to_message_id=reply_to_message_id,
                         link_preview_options=LinkPreviewOptions(is_disabled=True))
    )
    return msg_info.id

def run():
    parser = argparse.ArgumentParser(description=r'''Echoo: A tool let's your program echo to Telegram.''')

    parser.add_argument("-t", "--token", default=None, type=str, help="Token for your bot.")
    parser.add_argument("-id", "--chat_id", default=None, type=str, help="Chat_id of your audience.")
    parser.add_argument("--parse-mode", default="Markdown", type=str, help='''Send Markdown or HTML, if you want Telegram apps to show bold,
                italic, fixed-width text or inline URLs in your bot's message''')
    parser.add_argument("-rid", "--reply-to-id", default=None, type=int, help='''''')
    parser.add_argument("--return-id", action="store_true")
    parser.add_argument("msg", default="Are u ok?", type=str, help="Message to send")

    args = parser.parse_args()
    if args.token is None:
        args.token = os.environ.get("TG_TOKEN", None)

    if args.chat_id is None:
        args.chat_id = os.environ.get("TG_CHAT_ID", None)

    if args.token is None or args.chat_id is None:
        warnings.warn("Echoo to telegram will not work. Neither --token nor TG_TOKEN is set. Neither --chat_id nor TG_CHAT_ID is set.")
        print(f"\033[32m[Echoo]\033[0m:" + f"\033[1m{args.msg}\033[0m")
        return
    
    tid = main(token=args.token, chat_id=args.chat_id, msg=args.msg, 
              parse_mode=args.parse_mode, reply_to_message_id=args.reply_to_id)
    
    if args.return_id:
        print(tid)


if __name__ == '__main__':
    run()
