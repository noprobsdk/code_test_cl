import requests
import json
import csv
##import pandas as pd
##Setup - Start
finishedHTMLString = ""
count = 0
url = "https://i.thonhotels.no/pub/sf/FormLink?_ri_=X0Gzc2X%3DAQpglLjHJlTQGkj48Jzb15yuAIPol4glMnyNzeweOReTlDTzaEAyiJwwnagf0zbvLjGVXyjLNpLOfhKLX%3DjLpkLxHNLgHggLgNLjKLgQghVXMtX%3DAQpglLjHJlTQGkj48Jzb15yuAIPol4glMnyNMSh8D17tza0mWUqfpywqNGlGqW5kJ&_ei_=Erdv7PMYfAm0WU0r9JH49_wmGS4.&_di_=t61475eoe4q8sm30kdnv2a5src77j1tgcqjvlp95rh6e65fep620RS_ENDPOINThttps://login2.responsys.netRS_PASSWORDkioSDKAQ8390dj!kjcvjhdKjdyuzshstyRS_USERNAMEAPI@ARCHIVE"
## Parse data here
data = requests.get(url)
jsonparse = data.json()
data = jsonparse['data']
##Setup - End
cl_data = []
## Assemble new list - Start
for i in data:
    if i['table'] == "CONTACTS_LIST":
        #print (i)
        cl_data.append(i)
    #else:
## Assemble new list - End
#print (cl_data)
## Assemble list of HTML data - Start
for i in cl_data:
    ## Header of html and table
    strTable = "<html><H2>Table number:"+ str(count) +"</H2><table><tr><th>#</th><th>Folder</th><th>Table_</th><th>Riid</th></tr>"
    ## Table row
    strRaw = "<tr><td>" + str(count) + "</td><td>" + str(i['folder']) + "</td><td>" + str(i['table']) + "</td><td>" + str(i['riid_']) +"</td></tr>"
    ##Assemble table head with table row nth
    finishedHTMLString += strTable + strRaw
    count+=1
## Assemble list of HTML data - End
print(finishedHTMLString)
##Save as html file
hs = open("test7.html","w")
hs.write(finishedHTMLString)
hs.close()