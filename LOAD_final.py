import json
import requests
import pprint







# Aufruf von API Plusserver https://api.nexinto.com/v2/docs/swagger

def stern():                                         # Definition der Funktion Stern() zur Ausgabe von Platzhaltern
    print('******************************************************************************************************************************************')
        
h = {                                                # Definition Variable h mit Headerdaten aus der API
    "accept": "application/json",
    "Content-Type": "application/json"
}

p = {                                                # Definition Variable p mit Bodydaten (Data) aus der API
    'username': 'nifapi.nordex@nordex-online.com',
    'password': 'Nordex123!'
  }



r = requests.post('https://api.nexinto.com/v2/api/authentication/token',headers=h, data=json.dumps(p))   # request auf URL mit Angabe des Headers (h) und Bodys/Payloads (p)




pprint.pprint(r.json())                              # pprint.pprint() als Funktion zur Formatierung der Ausgabe (pretty print)
stern()

s = r.json()                                         # erzeugt in s ein Dictionary aus r (JSON Format)
x = s.get("accessToken")                             # Dict (Key:Value)   holt (get) den Wert (Value) aus s(Dict) an der Stelle 'accessToken'(Key) und schreibe ihn in x
y = s.get("refreshToken") 

t = {
    "accessToken": x,
    "refreshToken": y
}  

m = {
    'accept': 'application/json',
    'x-accesstoken': x
}

d = requests.get('https://api.nexinto.com/v2/api/monitoring/services/f6a0f602-65eb-4c4e-8b8e-b9578684e987', headers=m).text

v = json.loads(d)



o = requests.post('https://api.nexinto.com/v2/api/authentication/logout', headers=h, data=json.dumps(t))

alarmText = ' statusSince: ' + v['statusSince'] + ' | ' + 'statusInfo: ' + v['statusInfo']

print(alarmText)








