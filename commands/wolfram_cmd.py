from bot import command, msg
import xml.etree.ElementTree as ET
import urllib.parse

BASE_URL = 'http://api.wolframalpha.com/v2/query?format=plaintext'

class WolframCmd(command.BotCommand):
	def run(self, dest, contents):
		if len(contents) < 2:
			return msg.BotMsg('Usage: .wolfram [search terms]')

		search_str = ' '.join(contents[1:])
		url = BASE_URL + '&appid=' + self._app_id
		url += '&input=' + urllib.parse.quote(search_str)
		tree = self.xml_from_url(url)
		try:
			for child in tree:
				if 'primary' in child.attrib:
					text = child[0][0].text
					return msg.BotMsg(text)
		except:
			# Ignore all exceptions.
			pass

		return msg.BotMsg('No results found.')

	def xml_from_url(self, url):
		res = urllib.request.urlopen(url)
		body = res.read().decode()
		return ET.fromstring(body)

	def set_bot_config(self, cfg):
		super().set_bot_config(cfg)
		name = self.get_attribute('name')
		wolfram_cfg = self._bot_config[name]
		if 'app-id' not in wolfram_cfg:
			self._attributes['enabled'] = False
			return

		self._app_id = wolfram_cfg['app-id']

command_instance = WolframCmd(bindings = ['wolfram'], name = 'wolfram')