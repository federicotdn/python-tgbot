import random

from bot import command, msg

class RandLineCmd(command.BotCommand):
	def run(self, dest, contents):
		lines = self._bindings_map[contents[0][1:]]
		return msg.BotMsg(random.choice(lines).strip())

	def set_bot_config(self, cfg):
		super().set_bot_config(cfg)
		name = self.get_attribute('name')
		files_cfg = self._bot_config[name]

		self._bindings_map = {}
		for val in files_cfg.values():
			filename, binding = [p.strip() for p in val.split(',')]
			with open(filename) as f:
				self._bindings_map[binding] = f.readlines()
				self._attributes['bindings'].append(binding)

command_instance = RandLineCmd(name = 'rand_line')