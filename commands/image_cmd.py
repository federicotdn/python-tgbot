import os, shutil, urllib.request, urllib.parse, json
from bot import command, msg, image

class ImgCmd(command.BotCommand):
	def run(self, dest, contents):
		if len(contents) < 2:
			return msg.BotMsg('Usage: .image [search terms]')

		base_url = 'https://www.googleapis.com/customsearch/v1?searchType=image&safe=medium'
		base_url += '&cx=' + self._google_cx + '&key=' + self._google_api_key
		search_str = ' '.join(contents[1:])
		base_url += '&q=' + urllib.parse.quote(search_str)
		data = self.json_from_url(base_url)

		if not 'items' in data:
			return msg.BotMsg('No images found.')

		for item in data['items']:
			link = item['link']
			if link.endswith('.jpg') or link.endswith('.png'):
				file_name = 'image.' + link.split('.')[-1]
				try:
					response = urllib.request.urlopen(link)
					out_file = open(file_name, 'wb')
					shutil.copyfileobj(response, out_file)
					out_file.close()

					return image.BotImage(file_name)
				except:
					# Ignore all exceptions, try with next image result.
					pass

		return msg.BotMsg('No images found.')

	def json_from_url(self, url):
		res = urllib.request.urlopen(url)
		body = res.read().decode()
		return json.loads(body)

	def set_bot_config(self, cfg):
		super().set_bot_config(cfg)
		self._google_cx = self._bot_config['image']['google-cx']
		self._google_api_key = self._bot_config['image']['google-api-key']

command_instance = ImgCmd(commands = ['image', 'i'], name = 'image')
