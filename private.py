import os
from dotenv import load_dotenv
import httpx
import json

load_dotenv()

USERNAME = 'rafal-mi'

PERSONAL_ACCESS_TOKEN = os.getenv("PERSONAL_ACCESS_TOKEN")

headers = {
    "Authorization": f"token {PERSONAL_ACCESS_TOKEN}"
}

URL = f"https://api.github.com/repos/{USERNAME}/blender-tutorials"

response = httpx.get(URL, headers=headers)

print(response.status_code)

s = json.dumps(response.json(), indent=2)
print(s)


