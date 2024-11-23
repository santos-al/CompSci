import re

url = input("URL: ").strip()

print(url)

matches = re.search(r"^https?://(?www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)

if matches:
    print(f"Username: {matches.group(1)}")

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(username)