import requests
import json
import csv
import os.path
##import pandas as pd
count = 0
url = "https://i.thonhotels.no/pub/sf/FormLink?_ri_=X0Gzc2X%3DAQpglLjHJlTQGkj48Jzb15yuAIPol4glMnyNzeweOReTlDTzaEAyiJwwnagf0zbvLjGVXyjLNpLOfhKLX%3DjLpkLxHNLgHggLgNLjKLgQghVXMtX%3DAQpglLjHJlTQGkj48Jzb15yuAIPol4glMnyNMSh8D17tza0mWUqfpywqNGlGqW5kJ&_ei_=Erdv7PMYfAm0WU0r9JH49_wmGS4.&_di_=t61475eoe4q8sm30kdnv2a5src77j1tgcqjvlp95rh6e65fep620RS_ENDPOINThttps://login2.responsys.netRS_PASSWORDkioSDKAQ8390dj!kjcvjhdKjdyuzshstyRS_USERNAMEAPI@ARCHIVE"
## Parse data here
data = requests.get(url)
jsonparse = data.json()
data = jsonparse['data']
## Parse data ends
## Setup table for HTML
strTable = "<html><table><tr><th>#</th><th>Folder</th><th>Table_</th><th>Riid</th></tr>"
## Get values from json object
for i in data:
    ##Parse values to table rows
    ##print(i['folder'])
    ##print(i['table'])
    ##print(i['riid_'])
    strRaw = "<tr><td>" + str(count) + "</td><td>" + str(i['folder']) + "</td><td>" + str(i['table']) + "</td><td>" + str(i['riid_']) +"</td></tr>"
    ##Assemble table head with table row nth
    strTable = strTable + strRaw
    count += 1
##Finish bottom of html table
strTable = strTable+"</table></html>"
##Print to terminal
if
print(strTable)
##Save as html file
hs = open("test6.html","w")
hs.write(strTable)
hs.close()