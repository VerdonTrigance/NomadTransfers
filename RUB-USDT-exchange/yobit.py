import yobit_api

def get_rate():
    res = yobit_api.PublicApi().get_pair_ticker(pair="rur_usdt")
    print(res['last'])

get_rate