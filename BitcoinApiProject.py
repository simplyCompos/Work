import requests

url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "usd"
}

response = requests.get(url, params=params)

print("STATUS:", response.status_code)
print("HEADERS:", response.headers)
print("BODY:", response.json())

post_url = "https://httpbin.org/post"
data = {
    "name": "CryptoUser",
    "action": "test POST"
}

post_response = requests.post(post_url, json=data)

print("\nPOST STATUS:", post_response.status_code)
print("POST BODY:", post_response.json())
