import requests
import json
import csv
##import pandas as pd
##Setup - Start
finishedHTMLString = ""
count = 0
work = True
url = "https://i.thonhotels.no/pub/sf/FormLink?_ri_=X0Gzc2X%3DAQpglLjHJlTQGkj48Jzb15yuAIPol4glMnyNzeweOReTlDTzaEAyiJwwnagf0zbvLjGVXyjLNpLOfhKLX%3DjLpkLxHNLgHggLgNLjKLgQghVXMtX%3DAQpglLjHJlTQGkj48Jzb15yuAIPol4glMnyNMSh8D17tza0mWUqfpywqNGlGqW5kJ&_ei_=Erdv7PMYfAm0WU0r9JH49_wmGS4.&_di_=t61475eoe4q8sm30kdnv2a5src77j1tgcqjvlp95rh6e65fep620RS_ENDPOINThttps://login2.responsys.netRS_PASSWORDkioSDKAQ8390dj!kjcvjhdKjdyuzshstyRS_USERNAMEAPI@ARCHIVE"
## Parse data here
data = requests.get(url)
jsonparse = data.json()
data = jsonparse['data']
headers = ['TH_SALE_SUBSCRIBERS', 'CONTACTS_LIST', 'TH_BENELUX', 'TE_STAKEHOLDERS']
##Setup - End

## Assemble new list - Start
for header in headers:
    strTable = "<html><table><tr><th>#</th><th>Folder</th><th>Table_</th><th>Riid</th></tr>"
    for item in data:
        if header == item['table']:
            strRaw = "<tr><td>" + str(count) + "</td><td>" + str(item['folder']) + "</td><td>" + str(item['table']) + "</td><td>" + str(item['riid_']) +"</td></tr>"
            count += 1
            strTable = strTable + strRaw
    count = 0
    finishedHTMLString = finishedHTMLString + strTable
#fulllist = cl_data_ContactsList + sale_data + benelus_data_List + stakeholder_data_list
## Assemble new list - End
#print (cl_data)
## Assemble list of HTML data - Start

## Assemble list of HTML data - End
print(finishedHTMLString)
##Save as html file
hs = open("test7.html","w")
hs.write(finishedHTMLString)
hs.close()