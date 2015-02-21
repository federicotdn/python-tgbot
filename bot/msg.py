from bot import reply

class BotMsg(reply.BotReply):
	def __init__(self, msg):
		self._msg_list = [msg]

	def add_line(self, msg):
		self._msg_list.append(msg)

	def send_reply(self, dest, tg_socket):
		for msg in self._msg_list:
			final_msg = 'msg ' + dest + ' ' + reply.BOT_PREFIX + msg + reply.BOT_SUFFIX
			tg_socket.sendall(final_msg.encode())
