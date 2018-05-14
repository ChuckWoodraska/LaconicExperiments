from Robinhood import Robinhood
from chuck_pyutils import core as utils
import pprint
import quandl
from datetime import datetime

config = utils.read_config(utils.get_file_path(__file__, 'config.ini'))

quandl.ApiConfig.api_key = config['QUANDL']['api_key']
{'HYI': 12}
my_trader = Robinhood()
logged_in = my_trader.login(username=config['ROBINHOOD']['username'], password=config['ROBINHOOD']['password'])

# current_price / (div_freq * div_payout)
# pprint.pprint(my_trader.securities_owned())
# for security in my_trader.securities_owned()['results']:
#     pprint.pprint(security['instrument'].split('/')[-2])
#     symbol = my_trader.instrument(security['instrument'].split('/')[-2])['symbol']
#     print(symbol)
def calculate_total_div_for_year(my_trader):
    total_amount = 0
    for div in my_trader.dividends()['results']:
        print(div)
        if datetime.strptime(div['payable_date'], '%Y-%m-%d') >= datetime(2018, 1, 1):
            print(div['payable_date'])
            total_amount += float(div['amount'])
    print(total_amount)
    print(total_amount/12)
# # stock_instrument = my_trader.securities_owned()
# # pprint.pprint(stock_instrument)
#     try:
#         mydata = quandl.get_table('ZACKS/DA', ticker=symbol)
#         x = mydata.iad[0]
#         y = mydata.div_freq_code[0]
#         z = mydata.div_amt[0]
#         print(mydata.div_freq_code)
#         print(mydata.iad)
#         print(mydata.div_amt)
#     except:
#         pass
import requests

# Request: Market Quotes (https://sandbox.tradier.com/v1/markets/quotes?symbols=spy)


# # Headers
#
# headers = {"Accept":"application/json",
#            "Authorization":"Bearer "}
#
# # Send synchronously
#
# response = requests.get('https://api.tradier.com/beta/markets/fundamentals/dividends?symbols=AAPL', headers=headers)
# try:
#   content = response.text
#   # Success
#   print(content)
# except:
#   # Exception
#   print('Exception during request')

calculate_total_div_for_year(my_trader)