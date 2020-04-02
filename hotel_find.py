import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
products=[]
prices=[]
content=requests.get("https://www.makemytrip.com/hotels/hubli-hotels.html")
soup=BeautifulSoup(content)
for a in soup.findAll('div', attrs={'class':'makeFlex spaceBetween'}):
    name=a.find('p', attrs={'class':'latoBlack font22 blackText appendBottom12'})
    products.append(name.text)
for a in soup.findAll('div', attrs={'class':'padding20 makeFlex column'}):
    price=a.find('p', attrs={'class':'latoBlack font26 blackText appendBottom5'})
    prices.append(price.text)
df = pd.DataFrame({'Hotel Name':products,'Price':prices}) 
df.to_csv('Hotels.csv', index=False, encoding='utf-8')
