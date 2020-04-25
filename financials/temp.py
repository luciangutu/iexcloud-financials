import requests
import re
import json
from credentials import url, token

    # get the P/E Ratio from API
    def get_pe_ratio(symbol):
        per_url = url + "/stable/stock/" + ticker + "/stats/peRatio" + "?token=" + token
        # make the request
        s = requests.Session()
        r = s.get(per_url)
        return r.text

    # get the P/E Ratio from API
    def get_ttmeps(symbol):
        eps_url = url + "/stable/stock/" + ticker + "/stats/ttmEPS" + "?token=" + token
        # make the request
        s = requests.Session()
        r = s.get(eps_url)
        return r.text

    def display_financials(felement):
        # https://sandbox.iexapis.com/stable/stock/IBM/financials/2?token=Tsk_974c2b98c67e47f5b92bd7d6cfe869c0&period=annual
        full_url = url + "/stable/stock/" + ticker + "/" + felement + "/" + years_behind + "?token=" + token + "&period" \
                                                                                                               "=annual "
        # make the request
        s = requests.Session()
        r = s.get(full_url)

        json_data = json.loads(r.text)

        # don't show the following data
        dont_display = ['currency', 'fiscalDate', 'reportDate']

        # remove non alphanumeric characters (url has balance-sheet, but the JSON has balancesheet)
        felement = re.sub(r'\W+', '', felement)
        for i in range(int(years_behind)):
            # getting only the year
            full_date = json_data[felement][i]["fiscalDate"]
            short_date = full_date.split('-')[0]
            print(bcolors.OKBLUE + short_date + bcolors.ENDC)
            for k, v in json_data[felement][i].items():
                if k not in dont_display:
                    print("{: >25} {: >25}".format(k, v))
                    with sqlite3.connect("db/" + ticker + '.db') as conn:
                        c = conn.cursor()
                        # Insert data into SQLite
                        c.execute('INSERT INTO stocks VALUES (?, ?, ?)', (short_date, k, v))
                        conn.commit()


def return_financials():
    # SQLITE
    with sqlite3.connect("db/" + ticker + '.db') as conn:
        c = conn.cursor()
        # check if table exists
        c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='stocks'")
        if c.fetchone()[0] != 1:
            # Create table
            sql_cmd = 'CREATE TABLE stocks (date text, key text, value real)'
            c.execute(sql_cmd)
        conn.commit()

    financials = ['financials', 'balance-sheet', 'cash-flow', 'income']
    for f in financials:
        print("<br>")
        print(Format.underline + f.upper() + Format.end)
        display_financials(f)
    print(get_pe_ratio(ticker))
    print(get_ttmeps(ticker))