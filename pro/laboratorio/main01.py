#
#
import requests

r = requests.get('https://httpbin.org/ip')

print(r.headers)
print (r.status_code)
print(r.encoding)
print(r.content)
print(r.text)
