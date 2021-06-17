import requests

r = requests.post('https://api.github.com', data = {'key':'value'})

print(r)
print(r.json())
print(r.text)