URL_String=raw_input("Please enter your Pinterest board url {https://www.pinterest.com/username/board-slug}: ")

from Tkinter import *
import tkFileDialog as filedialog
FOLDER_URL=filedialog.askdirectory(title="Select the folder where you want to save the images: ")
if FOLDER_URL=='':
    print('Folder not selected')
    exit(0)
from lxml import html
import requests

page=requests.get(URL_String)
print(page.status_code)
tree=html.fromstring(page.content)

print(tree)
pins=tree.xpath('.//div[@class="GrowthUnauthPinImage"]/a/@href')
import requests, bs4
import urllib
print("Pin from board " + URL_String + " will be saved on " + FOLDER_URL)
print("Array of pins in board")
print(pins)
print("Total number of pins " + str(len(pins)))
n=1
for pin in pins:
  print("Saving Image Number: " + str(n))
  page=requests.get('http://www.pinterest.com'+pin)
  print("Pin " + pin + " processed")
  page_soup=bs4.BeautifulSoup(page.text,"lxml")
  page_element=page_soup.select('img[src]')
  image_address=page_element[0].attrs['src']
  image_title = page_element[0].attrs['alt']
  if len(image_title) < 2:
      image_title=str(n)
  resource=urllib.urlopen(image_address)
  output=open(FOLDER_URL+"/"+"Image"+image_title[:50]+".jpg","wb")
  output.write(resource.read())
  output.close()

  n=n+1
