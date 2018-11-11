from bot import Telegram_bot
from thirukural import Daily_Thirukural
import random

bot = Telegram_bot('config.cfg')

def make_reply(message):
	kural = Daily_Thirukural("config.cfg")
	return kural.get_kural()
	
update_id = None
while True:
	updates = bot.get_updates(offset=update_id)
	updates = updates["result"]
	if updates:
		for item in updates:
			update_id = item["update_id"]
			try:
				message = str(item["message"]["text"])
			except:
				message = None
			from_ = item["message"]["from"]["id"]
			reply = make_reply(message)
			bot.send_message(reply, from_)