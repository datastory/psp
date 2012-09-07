import urllib2
from bs4 import BeautifulSoup

# cilovy soubor
f = open("hlasy.csv", "w")

# adresa vysledku hlasovani
url = "http://psp.cz/ff/d9/64/ec/16.htm"
page = urllib2.urlopen(url)

soup = BeautifulSoup(page, from_encoding="windows-1250")

def remove(soup, tagname):
    for tag in soup.findAll(tagname):
        contents = tag.contents
        parent = tag.parent
        tag.extract()

remove(soup, "h2")
remove(soup, "tr")

vote_len = soup.find_all("span", class_="flag")

for x in range(0,len(vote_len)):
	vote = soup.find_all("span", class_="flag")[x].string
	name = vote.find_next("a").string

	f.write(name.encode("utf-8") + "," + vote.encode("utf-8") + "\n")
	print("Zapisuji " + str(x) + ". zaznam.")

f.close()