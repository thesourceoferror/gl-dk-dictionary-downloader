import requests
import os
from lxml import etree
import time
from tqdm import tqdm

class Collect:

	def __init__(self):
		self.link = "http://ilinniusiorfik.gl/oqaatsit/daka"
		self.data = {'f': 'cc', 'l': '0', 'c': '500', 'p': '500', 'e0': '', 'e1': ''}
		self.headers = {'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Accept': '*/*', 'Origin': 'http://ilinniusiorfik.gl', 'Referer': 'http://ilinniusiorfik.gl/oqaatsit/daka', 'Accept-Language': 'da-GL,da-DK;q=0.9,da;q=0.8,en-US;q=0.7,en;q=0.6'}

	def get(self, index):
		self.data['c']=index
		self.data['p']=index

		response = requests.post(self.link, data=self.data, headers=self.headers, verify=False)

		return response.text

	def format(self, response):
		tree = etree.fromstring(response.encode("utf-8"))

		gl_word = tree.xpath("/daka/div/p/b/text()")

		dk_trans = tree.xpath("/daka/div/p/text()")

		dk_trans.sort(key=len, reverse=True)

		dk_trans = dk_trans[0]

		pair = {"GL": gl_word[0].strip(), "DK": dk_trans.strip()}

		return pair

	def get_pair(self,index):
		response = self.get(index)
		formatted = self.format(response)

		return formatted

cllct = Collect()

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path os.path.join(dir_path, "dictionary.txt")

def save_contents():
	with open(file_path, "a") as myfile:
		for i in tqdm(range(18574)):
			resp = cllct.get_pair(i)
			myfile.write(resp["GL"] + "\t\t" + resp["DK"]+"\n")

def debug_f():
	while(1):
		number = input("Value: ")
		print(cllct.get_pair(number))

save_contents()
