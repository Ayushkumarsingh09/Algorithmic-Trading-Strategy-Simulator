import requests

class LiveTrading:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def place_order(self, symbol, quantity, side):
        url = f"https://api.example.com/order"
        payload = {"symbol": symbol, "quantity": quantity, "side": side}
        response = requests.post(url, json=payload, headers={"Authorization": f"Bearer {self.api_key}"})
        return response.json()
