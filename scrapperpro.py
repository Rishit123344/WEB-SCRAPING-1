from bs4 import BeautifulSoup as bs
import requests
import pandas as pd 
brightstarsurl = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page = requests.get(brightstarsurl)
soup = bs(page.text,'html.parser')
starttable = soup.find('table')
templist = []
tablerows = starttable.find_all('tr')
for tr in tablerows :
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    templist.append(row)
starnames = []
mass = [] 
distance = []
radius = []
lum = []   
for i in range(1,len(templist)):
    starnames.append(templist[i][1])
    distance.append(templist[i][3])
    mass.append(templist[i][5])
    radius.append(templist[i][6])
    lum.append(templist[i][7])
df = pd.DataFrame(list(zip(starnames,mass,distance,radius,lum)),columns = ['starnames','mass','distance','radius','lum'])
print(df)
df.to_csv('brightstars.csv')
