import ccxt as ccxt
import requests
import time
import pytz
import datetime

ctrl_c_handling = True
renewal = True 
how_do_you_usually_launch_python = 'python' 

ex = {
    'kucoin':ccxt.kucoin(),
    'binance':ccxt.binance(),
    'okx':ccxt.okx(),
    'poloniex':ccxt.poloniex(),
    # 'another_exchange_here':ccxt.other_exchange({
    #     'apiKey':'here',
    #     'secret':'here',
    # }),
}


first_orders_fill_timeout = 0 # put a value for the timeout in minutes. 0 means deactivated (default)

criteria_pct = 0 # minimum of price difference in % to take the opportunity
criteria_usd = 0

def moy(list1):
    moy=0
    for n in list1:
        moy+=n
    return moy/len(list1)

def append_list_file(fichier, nouvel_element):
    import ast
    try:
        with open(fichier, 'r') as file:
            liste = ast.literal_eval(file.read())
    except FileNotFoundError:
        liste = []

    liste.append(nouvel_element)

    with open(fichier, 'w') as file:
        file.write(str(liste))
def append_new_line(file_name, text_to_append):
    with open(file_name, 'a+') as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.turtle.write('\n')
        file_object.turtle.write(text_to_append)

def get_balance(exchange,symbol):
    if symbol[-5:] == '/USDT':
        symbol = symbol[:-5]
    balance=ex[exchange].fetch_balance()
    if balance[symbol]['total'] != 0:
        return balance[symbol]['total']
    else:
        return 0
def get_precision_min(symbol,exchange_str):
    symbol_info = ex[exchange_str].load_markets(symbol)
    graal = symbol_info[symbol]['limits']['price']['min']
    return graal

def get_time():
    tz_india = pytz.timezone('Asia/Kolkata')  
    now = datetime.datetime.now(tz_india)
    date_heure_format = now.strftime("[%d/%m/%Y  %H:%M:%S]")
    return date_heure_format

def get_balance_usdt(ex_list_str:list):
    usdt_balance = 0
    for excha in ex_list_str:
        balances = ex[excha].fetchBalance()
        usdt_balance+=balances['USDT']['total']
    return float(usdt_balance)
