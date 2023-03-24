import requests

r = requests.get('https://www.frcon.utn.edu.ar/galileo/downld02.txt')

#print(r.headers)
#print (r.status_code)
#print(r.encoding)
#print(r.content)
#print(r.text)
tem = r.text
l = tem.split(" \r\n")
a=l[-2]
x = str(a).split("  ")
p = x [0:3]


print(p)
 
