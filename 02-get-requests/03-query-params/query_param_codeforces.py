import requests

param = {
    "tags": "800-1000"
}
url = "https://codeforces.com/problemset"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

app = requests.get(url, params=param, headers=headers, timeout=15)

print(app.status_code)
print(app.text)   
