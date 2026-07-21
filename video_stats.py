import requests

API_KEY = ""
CHANNEL_HANDLE = "MrBeast"
url = f"https://youtube.googleapis.com/youtube/v3/channels?part=ContentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

response = requests.get(url)
print(response)
