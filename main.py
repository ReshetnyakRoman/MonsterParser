import requests
from bs4 import BeautifulSoup
import math
from config import searchCriteria


def getData(keys):
	r = s.get('https://www.monster.com/jobs/search/', params=keys, timeout=180)
	file = open('response.html','w')
	file.write(r.url+'\n')
	file.write(r.text)
	file.close()



#==========Initialization========
s = requests.Session()
keys = {'q':searchCriteria['position'],
		'where':searchCriteria['location'],
		'tm':searchCriteria['period'],
		'stpage':1,
		'page':1}


#==========Collecting data========

#First run to find-out number of pages in SERP:
getData(keys)

#calculating number of pages:
response = open('response.html','r')
soup1 = BeautifulSoup(response, 'html.parser')

totaData = soup1.find_all('div', class_='mux-search-results')
totalPositions = int(totaData[0]['data-results-total'])
posititonPerPage = int(totaData[0]['data-results-per-page'])
lastPage = math.ceil(totalPositions/posititonPerPage)

#updating number of last page in search parameters:
keys['page'] = lastPage

#Getting data for all postions with updated search params:
getData(keys)


#==========Parsing data========
with open('response.html','r') as htmlFile:
	soup2 = BeautifulSoup(htmlFile, 'html.parser')

positions = soup2.find_all('header', class_ = 'card-header')

file = open('positions.txt','w')

for item in positions:
	position = item.h2.a
	if position is not None:
		file.write(position.text)

file.close()


print('Complete! Total number of Positions: {}'.format(totalPositions))