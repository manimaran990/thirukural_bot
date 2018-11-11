import requests
import json
import configparser as cfg

class Telegram_bot(object):

	def __init__(self, config):
		self.token = self.read_token_from_config(config)
		self.base = "https://api.telegram.org/bot{}/".format(self.token)

	def get_updates(self, offset=None):
		url = self.base + "getUpdates?timeout=100"
		if offset:
			url = url + "&offset={}".format(offset+1)
		r = requests.get(url)
		return json.loads(r.content.decode("utf8"))

	def send_message(self, message, chat_id):
		url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, message)
		if message is not None:
			requests.get(url)

	def read_token_from_config(self, config):
		parser = cfg.ConfigParser()
		parser.read(config)
		return parser.get("creds","token")

	def thirukural_token(self, config):
		parser = cfg.ConfigParser()
		parser.read(config)
		return parser.get("creds", "thirukural_api")