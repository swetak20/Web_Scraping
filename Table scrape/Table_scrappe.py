import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
# table = soup.find('table', class_='wikitable')
# table_head = table.find_all('tr')
# for items in table_head:
#     data = items.find(['th'])
#     Heading = []
#     try:
#         Heading.append(data.text)
#     except IndexError: pass
#     print(Heading)

Symbol = []
Security = []
SEC_filings = []
GICS_sector = []
GICS_subsector = []
Headquarters_location = []
Date_first_added = []
CIK = []
Founded = []

heading = [Symbol, Security, SEC_filings, GICS_sector,GICS_subsector,Headquarters_location,Date_first_added,CIK,Founded]
for items in soup.find('table', class_='wikitable').find_all('tr')[1::1]:
    data = items.find_all(['td'])
    try:
        for i in range(len(heading)):
            heading[i].append(data[i].text.replace('\n', ' ').strip())
    except IndexError:pass



Table = []
for j in range(0,len(Symbol)):
    res = {"Symbol" :heading[0][j],
            "Security": heading[1][j],
            "SEC_filings" :heading[2][j],
            "GICS_sector" : heading[3][j],
            "GICS_subsector": heading[4][j],
            "Headquarters_location":heading[5][j],
            "Date_first_added":heading[6][j],
            "CIK":heading[7][j],
            "Founded":heading[8][j]}
    Table.append(res)
data = { 'data' : Table}
print(data)

# for k in range(5):
#     print(Table[k])
