import random
from commands.wikiquote import wikiquote
from bot import command, msg

class QuoteCmd(command.BotCommand):
	def run(self, dest, contents):
		if len(contents) < 2:
			return msg.BotMsg('Usage: .quote [search terms]')

		search_str = ' '.join(contents[1:])
		results = wikiquote.search(search_str)

		if not results:
			return msg.BotMsg('There were no results matching the query.')

		for result in results[:3]:
			try:
				quotes = wikiquote.quotes(result, 50)
				return msg.BotMsg('"' + random.choice(quotes) + '" - ' + result)
			except:
				# Ignore all exceptions, try with next result.
				pass

		return msg.BotMsg('Query was too ambiguous.')

command_instance = QuoteCmd(bindings = ['quote', 'q'], name = 'quote')
