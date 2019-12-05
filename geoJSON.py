import json;
import urllib.request, urllib.parse, urllib.error;
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input("Please enter a location: ")

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

params = dict()
params["address"] = address
params["key"] = 42

url = serviceurl + urllib.parse.urlencode(params)
print('Retrieving', url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

records = json.loads(data)

print("Place id ", records['results'][0]['place_id'])


