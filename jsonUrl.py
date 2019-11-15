import urllib.request, urllib.parse, urllib.error;
import json
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total = 0
url = input("Please enter a URL ")
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print(type(data))
recording = json.loads(data)
for item in recording['comments']:
    num = int(item['count'])
    total += num
print(total)
