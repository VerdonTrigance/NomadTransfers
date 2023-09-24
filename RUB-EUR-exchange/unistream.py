import requests

def get_RUB_EUR_rate():
    # The API endpoint
    url = "https://online.unistream.ru/api/card2cash/calculate?destination=SRB&amount=100000&currency=EUR&accepted_currency=RUB&profile=unistream&is_accepted_amount=1"
    headers = {
        'accept': '*/*', 
        'accept-encoding': 'gzip, deflate, br', 
        'accept-language': 'en,ru;q=0.9,sr;q=0.8', 
        'origin': 'https://unistream.ru', 
        'referer': 'https://unistream.ru/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'authorization': 'Bearer b960089fc2e1e2938a5d090fb218be9ff91ee5f0adb15fc6137a14b3b1bfb4dc'
    }
    # A GET request to the API
    response = requests.get(url, headers=headers)

    # Print the response
    response_json = response.json()
    rate = response_json['fees'][0]['rate']
    print(rate)

    return rate

get_RUB_EUR_rate()