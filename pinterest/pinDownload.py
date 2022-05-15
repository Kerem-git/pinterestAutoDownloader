import requests
from bs4 import BeautifulSoup
import wget


lines = open("pins.txt","r").readlines()

for url in lines:

    r = requests.get(url).text
    soup = BeautifulSoup(r,"lxml")
    f = str(soup.find_all(href=True)[6]).split('"')[3]
    out_filepath = "C:/SRC/images"  
    filename = wget.download(f, out=out_filepath)

    print(f)
