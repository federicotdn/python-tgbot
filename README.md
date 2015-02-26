# Python Telegram Bot

Bot for Telegram written in Python 3.4.  Uses the `wikipedia` and [`wikiquote`](https://github.com/federicotdn/python-wikiquotes) modules.

## Installation

Place the [`telegram-cli`](https://github.com/vysheng/tg) binary and your Telegram secret key (`telegram.key` text file) on the project's `bin` directory.  Start/stop the bot using the `tgbot-ctl` script:

```bash
$ chmod +x tgbot-ctl # make sure you can run the script
$ ./tgbot-ctl startbg # start the bot and detach it from the current terminal, 'start' will start the bot normally
$ ./tgbot-ctl stop # stop the bot
```

The bot is configured using the `bot.config` file.

Make sure to run `bin/telegram-cli -k bin/telegram.key` at least once before starting the bot, as you will need to setup your phone number first.

TODO: Finish writing instructions.

## Commands

- `flip_cmd.py`: returns 'heads' or 'tails' at random.
- `hello_cmd.py`: returns 'hello'.
- `image_cmd.py`: searches Google images, and uploads the first image found.  Requires two configuration variables to be set.  Get them at the [Google Custom Search](https://www.google.com/cse/all) site and at the [Google Developers Console](https://console.developers.google.com).
- `rand_line_cmd.py`: return a line from a text file at random.  The seed file/s need to be specified in the config file.
- `status_cmd.py`: print status information.
- `wikipedia_cmd.py`: returns a summary of the specified Wikipedia article.  Requires the `wikipedia` Python module (install it using `pip`).
- `quote_cmd.py`: returns a quote from the specified Wikiquote article.   Requires the `wikiquote` Python module (included as git submodule).

To disable a command, delete the corresponding `_cmd.py` file.
