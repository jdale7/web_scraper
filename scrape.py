import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://pittsburghpa.gov/mayor/press-releases.htm'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'blurbs': 'title'})

list_of_rows = []
for row in table.findAll('tr'):
	list_of_cells = []
	for cell in row.findAll('td'):
		list_of_cells.append(text)
	list_of_rows.append(list_of_cells)

outfile = open("./peduto_test.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)

print soup 

