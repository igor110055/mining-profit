# mining-profit
This tools helps you decide when to invest in bitcoin mining equipment


# INSTALL
```
git clone https://github.com/suchdatums/mining-profit.git
cd mining-profit

python3 -m venv .venv/
source .venv/bin/activate

pip install -r requirements.txt
```

# LUXOR API

https://github.com/LuxorLabs/hashrateindex-api-python-client

# EXAMPLES
```sh
python3 hashrateindex.py -k $LUXOR_API_KEY -f get_bitcoin_overview
python3 hashrateindex.py -k $LUXOR_API_KEY -f get_hashprice -p "_1_DAY",BTC
python3 hashrateindex.py -k $LUXOR_API_KEY -f get_network_hashrate -p "_3_MONTHS"
python3 hashrateindex.py -k $LUXOR_API_KEY -f get_network_difficulty -p "_3_MONTHS"
python3 hashrateindex.py -k $LUXOR_API_KEY -f get_ohlc_prices -p "_3_MONTHS"
python3 hashrateindex.py -k $LUXOR_API_KEY -f get_asic_price_index -p "_3_MONTHS",BTC
```
