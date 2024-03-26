import requests

link = 'http://127.0.0.1:5000/totalvalor'

r = requests.get(link)

print(r)
print(r.json())


