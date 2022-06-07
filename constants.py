
CLI_HELPTEXT = """
>> Remember: Ctrl-C to exit
"""

MAIN_TEXT = """# Open-Source Bitcoin Mining Profitability Calculator

__The goal of this project is to inspire__ people to learn more about bitcoin's built-in incentive structure - mining.

__The purpose of this tool is to__ help bitcoin miners make the best business decisions - how much to pay for equipment and what operating environment is needed to be profitable.
"""

HASH     = 1                            # 10**0
KILOHASH = 1_000                        # 10**3
MEGAHASH = 1_000_000                    # 10**6
GIGAHASH = 1_000_000_000                # 10**9
TERAHASH = 1_000_000_000_000            # 10**12
PETAHASH = 1_000_000_000_000_000        # 10**15
EXAHASH  = 1_000_000_000_000_000_000    # 10**18

# number of satoshi in one bitcoin
ONE_HUNDRED_MILLION = 100_000_000       # 10**8

# 6 blocks per hour, for 24 hours - assuming a perfect cadence of 10 minutes per block
EXPECTED_BLOCKS_PER_DAY = 144           # 24 * 6

# https://github.com/bitcoin/bitcoin/blob/0.21/src/chainparams.cpp#L69
SUBSIDY_HALVING_INTERVAL = 210_000

### DEFAULT NUMBERS FOR THE USER INPUT FIELDS
DEFAULT_POOL_FEE = 0 # per-cent (2 == 2%; 0.1 == 0.1%)
DEFAUL_KPKWH = 0.075 # dollars per kWh
DEFAULT_OPEX = 15 # dollars
DEFAULT_MONTHSTOPROJECT = 36
DEFAULT_PRICEGROW = 2
DEFAULT_PRICEGROW2 = 18
DEFAULT_LAG = 3
DEFAULT_HASHGROW = 3
DEFAULT_HASHGROW2 = -2
#DEFAULT_THRESHOLD = 1000000

# THESE ARE THE NAMES OF THE 'PIN' INPUT FIELDS
# MINER DETAIL INPUT FIELDS
PIN_COST = 'cost'
PIN_WATTAGE = 'wattage'
PIN_HASHRATE = 'hashrate'
PIN_BOUGHTATPRICE = 'boughtatprice'
# bitcoin price
PIN_BTC_PRICE_NOW = 'price'
PIN_PRICEGROW = 'pricegrow'
PIN_PRICEGROW_SLIDER = 'pricegrow_slider'
PIN_PRICEGROW2_SLIDER = 'pricegrow2_slider'
PIN_LAG = 'lag'
PIN_PRICEGROW2 = 'pricegrow2'
# miner analysis
PIN_CAPEX = 'satsPerTH'
PIN_COST_SLIDER = 'cost_slider'
PIN_EFF = 'eff'
PIN_EFF_SLIDER = 'eff_slider'
PIN_SAT_PER_TH = 'satsperth'
# bitcoina network state
PIN_HEIGHT = 'height'
PIN_AVERAGEFEE = 'avgfee'
PIN_NETWORKHASHRATE = 'nh'
PIN_HASHGROW = 'hashgrow'
PIN_HASHGROW_SLIDER = 'hashgrow_slider'
PIN_HASHGROW2 = 'hashgrow2'
# PROJECTION PARAMETERS
PIN_KWH_RATE = 'costkwh'
PIN_POOLFEE = 'poolfee'
PIN_OPEX = 'opex'
PIN_MONTHSTOPROJECT = 'months'
PIN_NEVERSELL = 'neversellmachine'
PIN_RESELL_UPPER ='resellupper'
PIN_RESELL_LOWER = 'reselllower'
PIN_UPPER_READONLY = 'upper_resale'
PIN_LOWER_READONLY = 'lower_resale'

# This is the option 'list' for the PIN_NEVERSELL checkbox
# Change this to change the text displayed
OPTION_NEVERSELL = "Never sell machine"

# THESE ARE DICTIONARY ITEM NAMES FOR THE RESULTS DICT WE CALCULATE
    ## CONSTANTS
KEY_MONTHS_TO_PROJECT = 'months'
KEY_START_HEIGHT = 'start height'
KEY_AVGFEE = 'avgfee'
KEY_MY_HASHRATE = 'my hashrate'
KEY_WATTAGE = 'wattage'
KEY_START_PRICE = 'start price'
KEY_PRICE_GROWTH = 'price growth'
KEY_PRICE_GROWTH2 = 'price grow2'
KEY_PRICE_LAG = 'price lag'
KEY_START_NH = 'starting nh'
KEY_HASH_GROWTH = 'hash growth'
#KEY_HASH_GROWTH2 : hashgrow2,
KEY_MONTHLY_OPEX = 'opex'
KEY_CAPEX = 'capex'
KEY_RESALE_UPPER = 'resale upper'
KEY_RESALE_LOWER = 'resale lower'
KEY_POOLFEE = 'poolfee'
KEY_RATE_KWH = 'rate kwh'
KEY_ESTIMATED_HEIGHT = 'height'
KEY_ESTIMATED_NETWORK_HASHRATE = 'network_hashrate'
KEY_ESTIMATED_PRICE = 'price btc'
KEY_HASHVALUE = 'hv'
KEY_KWH = 'kwh'
# THE SATS SOLD EVERY MONTH TO COVER THE GIVEN EXPENSE
KEY_SOLD_ELECTRICITY = 'sold_electricity'
KEY_SOLD_OPEX = 'sold_OPEX'
KEY_SOLD_CAPEX = 'sold_CAPEX'
KEY_BREAKEVEN_PRICE = 'BE price'
KEY_BREAKEVEN_PRICE_P20P = 'BE price 20%'
KEY_BREAKEVEN_NH = 'BE hashrate'
