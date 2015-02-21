from bot import reply

class BotImage(reply.BotReply):
	def __init__(self, image_path):
		self._image_path = image_path

	def send_reply(self, dest, tg_socket):
		final_msg = 'send_photo ' + dest + ' ' + self._image_path + reply.BOT_SUFFIX
		tg_socket.sendall(final_msg.encode())
