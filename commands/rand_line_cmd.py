import random

from bot import command, msg

class RandLineCmd(command.BotCommand):
	def run(self, dest, contents):
		if contents[0][1:] == 'fortune':
			return msg.BotMsg(random.choice(self.f1).strip())
		else:
			return msg.BotMsg(random.choice(self.f2).strip())

	def set_bot_config(self, cfg):
		super().set_bot_config(cfg)
		name = self.get_attribute('name')
		self.f1 = open(self._bot_config[name]['seed-path1']).readlines()
		self.f2 = open(self._bot_config[name]['seed-path2']).readlines()

command_instance = RandLineCmd(commands = ['mauro', 'fortune'], name = 'rand_line')
