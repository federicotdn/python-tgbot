BOT_PREFIX = '[bot] '
BOT_SUFFIX = '\n'

class BotReply:
	def send_reply(self, dest, tg_socket):
		raise NotImplementedError
