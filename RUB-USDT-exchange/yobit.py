import yobit_api
res = yobit_api.PublicApi().get_pair_ticker(pair="rur_usdt")
print(res['last'])