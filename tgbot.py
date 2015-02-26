import commands
import pkgutil
import socket
import sys
import configparser
import subprocess
import os.path
import time


CMD_FILE_SUFFIX = '_cmd'
CHEVRON_L = '<<<'
CHEVRON_R = '>>>'
DEFAULT_CFG_PATH = 'bot.config'
SOCK_NAME = 'telegram.socket'


def main():
	bot_cfg = read_bot_config()
	if not bot_cfg:
		print('Unable to load bot configuration.')
		sys.exit(1)

	cmd_dict = load_commands(bot_cfg)

	for key, val in cmd_dict.items():
		print('--> command ' + key + ' mapped to: ' + str(val))

	begin(cmd_dict, bot_cfg)


def read_bot_config():
	config_path = DEFAULT_CFG_PATH
	if len(sys.argv) == 2:
		config_path = sys.argv[1]
	print('Using config: ' + config_path)

	config = configparser.ConfigParser()
	try:
		config.read(config_path)
	except:
		return None
	return config


def load_commands(bot_cfg):
	cmd_dict = {}
	mods = pkgutil.iter_modules(commands.__path__, commands.__name__ + '.')

	for _, modname, _ in mods:
		if modname.endswith(CMD_FILE_SUFFIX):
			mod = __import__(modname, fromlist = True)

			if 'command_instance' not in dir(mod): # ignore old modules, remove later
				continue

			cmd_instance = mod.command_instance
			cmd_instance.set_bot_config(bot_cfg)

			enabled = cmd_instance.get_attribute('enabled')
			if not enabled:
				continue

			for cmd_name in cmd_instance.get_attribute('bindings'):
				cmd_dict[cmd_name] = cmd_instance

	return cmd_dict


def parse_msg(msg, cmd_prefix):
	if CHEVRON_L in msg or CHEVRON_R in msg:
		i = msg.index(CHEVRON_L) if CHEVRON_L in msg else msg.index(CHEVRON_R)
		dest = msg[1]
		contents = msg[i + 1:]
		cmd = contents[0]
		if cmd[0] != cmd_prefix or len(cmd) < 2:
			return None
		return (dest, contents, cmd[1:]) # dest = John_Smith, contents = New York, cmd[1:] = wiki


def read_line(tg_proc):
	try:
		if tg_proc.poll() is not None:
			raise Exception('telegram-cli has exited')
		line = tg_proc.stdout.readline().split()
		return [part.decode() for part in line]
	except:
		print('Pipe from telegram-cli closed, exiting.')
		sys.exit(0)


def start_telegram_cli(bot_cfg):
	cli_path = bot_cfg['bot']['cli-path'] + ' ' + bot_cfg['bot']['cli-args']
	print('Executing: ' + cli_path)

	try:
		proc = subprocess.Popen(cli_path.split(),
								stdout = subprocess.PIPE,
								stderr = subprocess.DEVNULL)
		# Give telegram-cli time to start the UNIX socket
		# TODO: use a better method to ensure socket exists
		time.sleep(1)

		if proc.poll() is not None:
			print('telegram-cli ended prematurely.')
			print('NOTE: Make sure socket "' + SOCK_NAME + '" does not exist already.')
			sys.exit(1)
		return proc
	except:
		print('Unable to start telegram-cli subprocess.')
		sys.exit(1)


def open_telegram_socket(bot_cfg):
	tg_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

	try:
		tg_socket.connect(SOCK_NAME)
		return tg_socket
	except:
		print('Unable to connect to telegram-cli socket (telegram.socket).')
		sys.exit(1)


def begin(cmd_dict, bot_cfg):
	tg_proc = start_telegram_cli(bot_cfg)
	cmd_prefix = bot_cfg['bot']['cmd-prefix']
	tg_socket = open_telegram_socket(bot_cfg)
	print('Setup complete, bot is now running.')

	while True:
		msg = read_line(tg_proc)
		print(msg)
		msg_parts = parse_msg(msg, cmd_prefix)

		if msg_parts:
			dest, contents, cmd = msg_parts
			if cmd in cmd_dict:
				cmd_instance = cmd_dict[cmd]
				reply = cmd_instance.run(dest, contents)
				if reply:
					reply.send_reply(dest, tg_socket)


if __name__ == '__main__':
	main()
