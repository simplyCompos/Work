import requests

def main():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    print("GET-запит:")
    print("Status code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.json())
    post_url = "https://httpbin.org/post"
    data = {"currency": "bitcoin", "amount": 1}
    post_response = requests.post(post_url, json=data)
    print("\nPOST-:")
    print("Status code:", post_response.status_code)
    print("Body:", post_response.json())

if name == "main":
    main()
