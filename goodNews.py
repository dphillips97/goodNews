# !python 3
# scrapes site for snippets and displays them randomly

from bs4 import BeautifulSoup 
import requests
import re
import random

# DONE
# extract text from each item 1-99


#TODO
# prettify text: remove initial and final quote marks
# choose random news_block
# return link for each item
# combine item and link

def soupify():
	url = r'https://qz.com/1169003/the-99-best-things-that-happened-in-2017/'
	page = requests.get(url)

	# create soup object
	# forgot to make page a text document
	page_doc = page.text
	soup = BeautifulSoup(page_doc, 'html.parser')
	
	# extract content
	# 'class' attribute in html is treated as a set 
	news_block = soup.find_all('p', attrs={'class':{'graf', 'graf-after--p'}})
	
	return news_block

def cleanup():
	news_block = soupify()
	for item in news_block:
		item_doc = item.text
		item_source = item_doc.split(' ')[-1]
		item_regex = re.compile(r'\d{1,2}\..+')
		item_out = item_regex.findall(item_doc)
		print(item_source)
		
cleanup()