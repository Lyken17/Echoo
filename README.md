# Echoo

Let your program echo to you.

## Installation

`pip install echoo`

## Usage

This tool is based on [Telegram](https://telegram.org) -- a secure and advanced IM. 

First, set your token([@bot_father](https://telegram.me/botfather)) and chat_id([@getidbot](https://telegram.me/getidsbot)) in environment.

Then, in command line

```echoo -m "Hello, how are you?"```. 

## Verbose

```bash
usage: echoo [-h] [-t TOKEN] [-id CHAT_ID] [-m MSG]

Echoo:: A tool let's your program echo.

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Token for your bot.
  -id CHAT_ID, --chat_id CHAT_ID
                        Chat_id of your audience.
  -m MSG, --msg MSG     Message to send
```