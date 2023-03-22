import httpx
import json

USERNAME = 'rafal-mi'

URL = f"https://api.github.com/users/{USERNAME}/repos"

response = httpx.get(URL)

for repo in response.json():
    print(repo["full_name"])

# s = json.dumps(response.json()[0], indent=2)
# print(s)
