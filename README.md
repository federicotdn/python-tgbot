# Python Telegram Bot (Dev branch)

Bot for Telegram written in Python 3.4.  Uses the `wikipedia` and [`wikiquote`](https://github.com/federicotdn/python-wikiquotes) modules.

## Installation

Place the [`telegram-cli`](https://github.com/vysheng/tg) binary and your Telegram secret key (key.txt) on the project's `bin` directory.  Start/stop the bot using the `tgbot` script:

```bash
$ chmod +x tgbot # make sure you can run the script
$ ./tgbot startbg # start the bot and detach it from the current terminal, 'start' will start the bot and show the output
$ ./tgbot stop # stop the bot
```

Make sure to run `bin/telegram-cli -k key.txt` at least once before starting the bot, as you will need to setup your phone number first.

## Commands

- `flip_cmd.py`: returns 'heads' or 'tails' at random.
- `fortune_cmd.py`: returns a phrase at random from a fortunes texts list.
- `hello_cmd.py`: returns 'hello'.
- `image_cmd.py`: searches Google images, and uploads the first image found.  **Requires** two environment variables to be set: `GOOGLE_CX` and `GOOGLE_API_KEY`.  Get them at the [Google Custom Search](https://www.google.com/cse/all) site and at the [Google Developers Console](https://console.developers.google.com).
- `rand_txt_cmd.py`: return a line from a text file at random.  **Requires** a `seed.txt` file to exist inside the `commands` directory.
- `status_cmd.py`: print status information.
- `wikipedia_cmd.py`: returns a summary of the specified Wikipedia article.  **Requires** the `wikipedia` Python module (install it using `pip`).
- `quote_cmd.py`: returns a quote from the specified Wikiquote article.   **Requires** the `wikiquote` Python module (included as git submodule).

To disable a command, delete the corresponding `_cmd.py` file.
