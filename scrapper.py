from bs4 import BeautifulSoup 
from urllib.request import Request, urlopen

URL = 'https://www.worldometers.info/coronavirus/'

req = Request(URL,headers={'User-Agent': 'Mozilla/5.0'})
with urlopen(req) as response:
    html_doc = response.read()


soup = BeautifulSoup(html_doc, 'html.parser')

countDict = {
    0: "country", 
    1: "total cases", 
    2: "new cases", 
    3: "total deaths", 
    4: "new deaths", 
    5: "total recovered", 
    6:  "active cases", 
    7: "serious"
}

def getDataCountryWise():
    countriesData = []
    elements = soup.find_all('tr',class_='')
    elements = elements[:len(elements)//2]
    for element in elements:
        data = {}
        count = 0
        for eachColumn in element.find_all('td'):
            if count<len(countDict.keys()):
                if eachColumn.find('a'):
                    countryName = eachColumn.find('a').get_text()
                    data[countDict[count]] = countryName
                else:
                    title = countDict[count]
                    data[title] = eachColumn.get_text()
                count+=1
        countriesData.append(data)
    return countriesData
    #element consists of eachRow 
    #now eachRow must be td so I need to get td of each tr
# Now let me make those data awesome!! 

