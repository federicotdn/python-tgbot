import wikipedia
from bot import command, msg

class WikiCmd(command.BotCommand):
	def run(self, dest, contents):
		if len(contents) < 2:
			return msg.BotMsg('Usage: .wiki [search terms]')

		search_str = ' '.join(contents[1:])
		results = wikipedia.search(search_str)

		if not results:
			return msg.BotMsg('There were no results matching the query.')

		try:
			summary = wikipedia.summary(results[0], sentences = 2)
		except wikipedia.exceptions.DisambiguationError as e:
			if not e.options:
				return msg.BotMsg('There were no results matching the query.')
			try:
				summary = wikipedia.summary(e.options[0], sentences = 2)
			except:
				return msg.BotMsg('Query was too ambiguous')

		return msg.BotMsg(summary)

command_instance = WikiCmd(bindings = ['wiki', 'w'], name = 'wiki')
