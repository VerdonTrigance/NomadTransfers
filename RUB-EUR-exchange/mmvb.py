import requests


def get_rate():
    # The API endpoint
    url = "https://iss.moex.com/iss/statistics/engines/currency/markets/selt/rates.json?iss.meta=off"

    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_json = response.json()
    reverse_rate = response_json["cbrf"]["data"][0][
        response_json["cbrf"]["columns"].index("CBRF_EUR_LAST")
    ]
    direct_rate = 1 / reverse_rate
    print(reverse_rate)
    print(direct_rate)

    return direct_rate


get_rate()
