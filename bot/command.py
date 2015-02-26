class BotCommand:

	_default_attributes = {
		'allow-speech': False,
		'bindings': [],
		'name': 'unnamed',
		'enabled': True
	}

	def __init__(self, **attributes):
		self._attributes = dict(self._default_attributes)
		for k, v in attributes.items():
			self._attributes[k] = v

	def run(self, dest, contents):
		raise NotImplementedError

	def get_attribute(self, attr):
		return self._attributes[attr]

	def set_bot_config(self, cfg):
		self._bot_config = cfg
