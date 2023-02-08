#pip3 install requests

import requests
with open('./wordlist.txt','r') as f:
    for line in f:
        url = 'http://3.145.94.96:8000/' + line.strip('\n')
        response = requests.get(url)
        #print(response.status_code)
        if response.status_code != 404:
            print(url)
