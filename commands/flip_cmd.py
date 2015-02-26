from bot import command, msg
import random

class FlipCmd(command.BotCommand):
	def run(self, dest, contents):
		if bool(random.getrandbits(1)):
			answer = 'Tails'
		else:
			answer = 'Heads'

		return msg.BotMsg('Coin flip: ' + answer)


command_instance = FlipCmd(bindings = ['flip'], name = 'flip')
