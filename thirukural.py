import configparser as cfg
import requests
import json

class Daily_Thirukural(object):
	def __init__(self, config):
		self.token = self.thirukural_token(config)
		self.BASE_URL = "https://getthirukkural.appspot.com/api/2.0/kural/rnd?appid={}&format=json".format(self.token)

	def thirukural_token(self, config):
		parser = cfg.ConfigParser()
		parser.read(config)
		return parser.get("creds", "thirukural_api")

	def get_kural(self):
		r = requests.get(self.BASE_URL)
		if r.status_code == 200:
			kurals = json.loads(r.content.decode("utf8"))['KuralSet']['Kural']	
			for kural in kurals:		
				number = kural['Number']
				line1 = kural['Line1']
				line2 = kural['Line2']
				meaning = kural['Translation']
				return "{}\n{}\n{}".format(number, line1+'\n'+line2, meaning)
		else:
			return ""

