import urllib.request, urllib.parse, urllib.error;
import xml.etree.ElementTree as ET;
import ssl;

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Please enter a URL: ")
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
counter = 0
total = 0
for item in lst:
    pre = int(item.find('count').text)
    # print(pre)
    total += pre
    counter += 1
print(total)
print(counter)

# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')
# print('User count:', len(lst))

# for item in lst:
#     print('Name', item.find('name').text)
#     print('Id', item.find('id').text)
#     print('Attribute', item.get('x'))