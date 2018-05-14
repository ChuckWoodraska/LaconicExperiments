from Robinhood import Robinhood
from chuck_pyutils import core as utils
import pprint
import quandl
from datetime import datetime

config = utils.read_config(utils.get_file_path(__file__, 'config.ini'))

quandl.ApiConfig.api_key = config['QUANDL']['api_key']

my_trader = Robinhood()
logged_in = my_trader.login(username=config['ROBINHOOD']['username'], password=config['ROBINHOOD']['password'])

# (div_freq * div_payout) / current_price
symbols_freq = {}
id_to_symbols = {}
div_rate = {}
for security in my_trader.securities_owned()['results']:
    instrument = my_trader.instrument(security['instrument'].split('/')[-2])
    symbol = instrument['symbol']
    id_to_symbols[security['instrument'].split('/')[-2]] = symbol
    symbols_freq[symbol] = {}
    quote = my_trader.quote_data(symbol)
    symbols_freq[symbol]['price'] = float(quote['last_trade_price'])
    try:
        mydata = quandl.get_table('ZACKS/DA', ticker=symbol)
        symbols_freq[symbol]['freq'] = mydata.div_freq_code[0]
        symbols_freq[symbol]['div_amt'] = mydata.div_amt[0]
        symbols_freq[symbol]['annual_amt'] = mydata.iad[0]
    except:
        symbols_freq[symbol]['freq'] = None
        symbols_freq[symbol]['div_amt'] = None
        symbols_freq[symbol]['ytd_amt'] = None

print(symbols_freq)
print(id_to_symbols)

for sym in symbols_freq:
    try:
        div_rate[sym] = (symbols_freq[sym]['freq'] * symbols_freq[sym]['div_amt']) / symbols_freq[sym]['price']
    except Exception as e:
        print(e)
pprint.pprint(div_rate)


def calculate_total_div_for_year(my_trader):
    total_amount = 0
    for div in my_trader.dividends()['results']:
        print(div)
        if datetime.strptime(div['payable_date'], '%Y-%m-%d') >= datetime(2018, 1, 1):
            print(div['payable_date'])
            total_amount += float(div['amount'])
    print(total_amount)
    print(total_amount / 12)

# calculate_total_div_for_year(my_trader)
