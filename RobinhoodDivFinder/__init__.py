# from Robinhood import Robinhood, endpoints
from chuck_pyutils import core as utils
import pprint
import quandl
from datetime import datetime
import dateutil

config = utils.read_config(utils.get_file_path(__file__, 'config.ini'))

# quandl.ApiConfig.api_key = config['QUANDL']['api_key']

# my_trader = Robinhood()
# logged_in = my_trader.login(username=x, password=config['ROBINHOOD']['password'])

import robin_stocks as r
login = r.authentication.login(config['ROBINHOOD']['username'], config['ROBINHOOD']['password'])
# print(login)
# positions_data = r.get_current_positions()
# for div in r.account.get_dividends():
#     print(div)
#
# print(r.account.get_total_dividends())
total_amount = 0
for x in r.account.get_dividends():
            # if datetime.strptime(div['payable_date'], '%Y-%m-%d') >= datetime(2018, 1, 1):
            #     print(div['payable_date'])
            #     c

    if x['paid_at']:
        # print(x)
        check_date = dateutil.parser.parse(x['paid_at']).date()
        if datetime(2020, 1, 1).date() >= check_date >= datetime(2018, 1, 1).date():
            total_amount += float(x['amount'])
print(total_amount)
print(total_amount / 24)
# my_stocks = r.build_holdings()
# for key,value in my_stocks.items():
#     print(key,value)
# (div_freq * div_payout) / current_price
# symbols_freq = {}
# id_to_symbols = {}
# div_rate = {}
# for security in my_trader.securities_owned()['results']:
#     instrument = my_trader.instrument(security['instrument'].split('/')[-2])
#     symbol = instrument['symbol']
#     id_to_symbols[security['instrument'].split('/')[-2]] = symbol
#     symbols_freq[symbol] = {}
#     quote = my_trader.quote_data(symbol)
#     symbols_freq[symbol]['price'] = float(quote['last_trade_price'])
#     try:
#         mydata = quandl.get_table('ZACKS/DA', ticker=symbol)
#         symbols_freq[symbol]['freq'] = mydata.div_freq_code[0]
#         symbols_freq[symbol]['div_amt'] = mydata.div_amt[0]
#         symbols_freq[symbol]['annual_amt'] = mydata.iad[0]
#     except:
#         symbols_freq[symbol]['freq'] = None
#         symbols_freq[symbol]['div_amt'] = None
#         symbols_freq[symbol]['ytd_amt'] = None
#
# print(symbols_freq)
# print(id_to_symbols)
#
# for sym in symbols_freq:
#     try:
#         div_rate[sym] = (symbols_freq[sym]['freq'] * symbols_freq[sym]['div_amt']) / symbols_freq[sym]['price']
#     except Exception as e:
#         print(e)
# pprint.pprint(div_rate)


# def calculate_total_div_for_year(my_trader):
#     total_amount = 0
#     for div in my_trader.dividends()['results']:
#         print(div)
#         if datetime.strptime(div['payable_date'], '%Y-%m-%d') >= datetime(2019, 1, 1):
#             print(div['payable_date'])
#             total_amount += float(div['amount'])
#     print(total_amount)
#     print(total_amount / 12)
#
#
# def calculate_total_div_alltime(my_trader):
#     total_amount = 0
#     for div in my_trader.dividends()['results']:
#         print(div)
#         total_amount += float(div['amount'])
#     print(total_amount)
#     print(total_amount / 12)
#
#
# def calculate_total_transfer(my_trader):
#     res = my_trader.session.get(endpoints.ach('transfers'))
#     res.raise_for_status()
#     res = res.json()
#     total_amount = 0
#     for t in res['results']:
#         print(t)
#         total_amount += float(t['amount'])
#     print(total_amount)


# calculate/_total_div_for_year(my_trader)
# calculate_total_div_alltime(my_trader)
# print(my_trader.get_account())


# if requesting all, return entire object so may paginate with ['next']

# calculate_total_transfer(my_trader)
# import requests
#
# response = requests.get('https://api.intrinio.com/data_point?identifier=AAPL&item=dividendyield')
# print(response.text)
