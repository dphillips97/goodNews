# !python 3
# scrapes site for snippets of good news and displays them randomly

from bs4 import BeautifulSoup 
import requests
import random


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
	
	# Empty list to store p elements
	item_list = []
	
	# Call function on page
	news_block = soupify()
	
	# For loop goes thru each 'p' in page object
	for item in news_block:
		
		# Create text object from soup object
		item_doc = item.text
		
		# add message to list
		item_list.append(item_doc)

	return item_list
	
def rand_choice(list_out):
	
	# print a random list item
	print(list_out[random.randint(1,99)])

	
list_entries = cleanup()
rand_choice(list_entries) 
