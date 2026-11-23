import requests

header = {
    "name" : "tarok"
}

re = requests.get("https://www.codeforces.com" , headers=header)
print(re.content)
