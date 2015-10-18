import urllib2
from bs4 import BeautifulSoup
import time

url = 'https://es.wikipedia.org/wiki/Pablo_Picasso'

html = urllib2.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

imgs = soup.findAll('img', src = True)
for img in imgs:
  print img['src']
  name = img['src'].split('/')[-1]
  print name
  image = open(name, "wb")
  download_img = urllib2.urlopen('https:' + img['src'])
  image.write(download_img.read())
  image.close()
  time.sleep(1)
