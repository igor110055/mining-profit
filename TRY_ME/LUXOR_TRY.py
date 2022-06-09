# https://hashrateindex.com/blog/energy-curtailment-strike-price-api/
# https://github.com/LuxorLabs/hashrateindex-api-python-client
# https://github.com/LuxorLabs/graphql-python-client
# https://data.hashrateindex.com/network-data/btc
# https://hashrateindex.com/



from luxordata import API

# 'keep it secret, keep it safe...'
import apikey

ENDPOINT = 'https://api.hashrateindex.com/graphql'

API = API(host=ENDPOINT, method='POST', key=apikey.LUXOR_API_KEY)


#data = API.get_bitcoin_overview()
# ['data']['bitcoinOverviews']['nodes']
"""
{'data':
    {'bitcoinOverviews':
        {'nodes':
            [
                {'timestamp': '2022-06-08T17:55:11+00:00',
                'hashpriceUsd': '0.12724264744230945',
                'networkHashrate7D': '218274685.4357019',
                'networkDiff': '30283293547736',
                'estDiffAdj': '40.19',
                'coinbaseRewards24H': '6.316474306214689',
                'feesBlocks24H': '1.0635888994350282',
                'marketcap': '578.82734242125',
                'nextHalvingCount': 100069,
                'nextHalvingDate': '2024-05-03T00:00:00+00:00',
                'txRateAvg7D': '2.8924172905095387'}]}}}
"""

#data = API.get_hashprice('_3_MONTHS', 'BTC')
# ['data']['getHashprice']['nodes']
"""
{'data':
    {'getHashprice':
        {'nodes':
            [
                {'timestamp': '2022-03-08T06:00:00+00:00', 'btcHashprice': 4.621846189553069e-06},
                ...
                {'timestamp': '2022-06-08T06:00:00+00:00', 'btcHashprice': 4.2434015547672876e-06}                
"""

#data = API.get_network_hashrate("_3_MONTHS")
# ['data']['getNetworkHashrate']['nodes']
"""
{'data':
    {'getNetworkHashrate':
        {'nodes':
            [
                {'timestamp': '2022-03-08T00:00:00+00:00', 'networkHashrate': 187.9989437279134},
                ...
                {'timestamp': '2022-06-08T00:00:00+00:00', 'networkHashrate': 242.24723058913494}
"""

#data = API.get_network_difficulty("_3_MONTHS")
# ['data']['getChartBySlug']['data']
"""
{'data':
    {'getChartBySlug':
        {'data':
            [
                {'time': '2022-03-08T12:00:16.392148+00:00', 'difficulty': 27.550332084343},
                ...
                {'time': '2022-06-08T10:00:16.392148+00:00', 'difficulty': 30.283293547736}
"""

# open, high, low, close price
# data = API.get_ohlc_prices("_3_MONTHS")
# ['data']['getChartBySlug']['data']
"""
{'data':
    {'getChartBySlug':
        {'data':
            [
                {'timestamp': '2022-03-08T00:00:00+00:00', 'open': 38987.39, 'high': 39040.42, 'low': 38950.13, 'close': 39015.8},
                ...
                {'timestamp': '2022-06-08T00:00:00+00:00', 'open': 31125.32, 'high': 31327.22, 'low': 29859.05, 'close': 30453.22}
"""

#data = API.get_asic_price_index("_3_MONTHS", 'BTC')
# ['data']['getChartBySlug']['data']
"""
{'data':
    {'getChartBySlug':
        {'data':
            [
                {'time': '2022-03-07T00:00:00+00:00', 'under38': 0.00220819, '_38to68': 0.00146849, 'above68': 0.0005764, 'close': 38025.2},
                ...
                {'time': '2022-06-08T00:00:00+00:00', 'under38': 0.0020847, '_38to68': 0.00121355, 'above68': 0.00058559, 'close': 31182.47}
"""


#print(data)
