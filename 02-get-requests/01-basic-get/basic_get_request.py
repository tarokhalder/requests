import requests

url = "https://www.codeforces.com"

response = requests.get(url=url)

print(response.status_code)
print(response.content)
