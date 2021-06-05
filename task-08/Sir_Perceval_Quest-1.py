import json
import os
import requests
page=1
while flag!=0:
    request = requests.get('https://api.github.com/users/amfoss/repos?page='+str(page))
    page+=1
    json = request.json()
    if len(json)==0:
        break
    for i in range(0,len(json)):
      os.system('perceval git --json-line '+json[i]['svn_url']+' >>commits.json')
