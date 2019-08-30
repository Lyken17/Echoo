# Echoo

Let your program echo to you~

## Installation

`pip install echoo`

OR 

`pip install --upgrade git+https://github.com/Lyken17/Echoo.git`


## Usage

This tool is based on [Telegram](https://telegram.org) -- a secure and advanced IM. 

First, set your token([@bot_father](https://telegram.me/botfather)) and chat_id([@getidbot](https://telegram.me/getidsbot)) in environment.

```
export TG_TOKEN=<your token here"
export TG_CHAT_ID=<your chat id here"
```


Then, find your bot in Telegram and enter `/start` to enable it  

In command line (same as `echo` in bash)

```echoo "Hello, how are you?"```. 

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
