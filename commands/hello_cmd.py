from bot import command, msg

class HelloCmd(command.BotCommand):
	def run(self, dest, contents):
		return msg.BotMsg('Hello there.')


command_instance = HelloCmd(commands = ['hello'], name = 'hello')
