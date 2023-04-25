import requests

API_KEY = "7fec778abd615a90f2dfc761221e2ded"


def get_data(place, days=None, options=None):
    url = f"api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))
