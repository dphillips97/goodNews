# !python 3
# scrapes site for snippets of good news and displays them randomly

from bs4 import BeautifulSoup 
import requests
import re
import random

# DONE
# extract text from each item 1-99
# prettify text: remove initial and final quote marks
# choose random news_block

#TODO
# Something weird is going on with the regex grouping for the body of the text 
# return link for each item
# return error message for specific text item

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
	
	item_list = []
	
	# Call function on page
	news_block = soupify()
	
	# For loop goes thru each 'p' on page (in HTML)
	for item in news_block:
		
		# Create text object from soup object
		item_doc = item.text
		
		# Create regex to extract groups from text
		# Add each item to a list and extract random list element
		match_obj = re.match(r'(\d{1,2}\.\s)(.+\.)', item_doc)
		
		#match_obj = re.match(r'^(\d{1,2}\.\s)(.+\.?+)', item_doc)
		
		try:
			# match number, return str
			item_number = match_obj.group(1)
						
			# match main message
			item_message = match_obj.group(2)
				
			# match 
			
			
			item_list.append(item_message)
		
		except:
			pass
	#move to newfunction
	rand = random.randint(1,99)
	print(item_list[rand])
	
cleanup()
