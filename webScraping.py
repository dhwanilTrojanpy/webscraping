import bs4
import requests
from bs4 import BeautifulSoup       
urls=[]
URL=requests.get("https://www.livecoinwatch.com")
parsedText=bs4.BeautifulSoup(URL.text,"lxml")
for i in parsedText.find_all("a",href=True):
    urls.append("https://www.livecoinwatch.com"+str(i["href"]))
urls=urls[17:67]    
def getPrice(url):
    URL1=requests.get(url)
    
    parsedTextFinal=bs4.BeautifulSoup(URL1.text,"lxml")
    
    name=parsedTextFinal.find_all("div",{"class":"mr20"})[0].find("h1").text
    
    s_name=parsedTextFinal.find_all("div",{"class":"mr20"})[0].find("p").text
    
    price=parsedTextFinal.find_all("div",{"class":"cion-item coin-price-large ml20 px-0"})[0].find("span").text
    
    capital=parsedTextFinal.find_all("div",{"class":"cion-item text-left"})[0].find("span").text
    
    volume=parsedTextFinal.find_all("div",{"class":"cion-item text-left"})[0].find("span").text
    
    liquidity=parsedTextFinal.find_all("div",{"class":"cion-item col-md-4 col-xl-3 px-1 py-1 py-md-0"})[0].find("span").text
    
    growth=parsedTextFinal.find_all("div",{"class":"cion-item px-1 grow"})[0].find("span").text
    
    print("{name:"+ str(name)+" shortname:"+ str(s_name)+" price:"+ str(price)+" capital:"+ str(capital)+" volume:"+ str(volume)+" liquidity:"+ str(liquidity)+" growth:"+ str(growth)+" }")

while True:
    for i in urls:
        getPrice(i)