from flask import render_template, url_for, flash, redirect, request
from financials import app, db
from financials.forms import HomeForm
from financials.models import Ticker
from credentials import url, token
from datetime import datetime
import requests
import re
import json


@app.route('/', methods=['GET', 'POST'])
def home():
    form = HomeForm()
    if form.validate_on_submit():
        ticker = Ticker.query.filter_by(stock=form.ticker.data).all()
        # make a list if it's only one element
        if not isinstance(ticker, list):
            ticker = [ticker]

        # update SQLite if checkbox is present
        if 'update' in request.form:
            financials = ['financials', 'balance-sheet', 'cash-flow', 'income']
            for f in financials:
                # https://sandbox.iexapis.com/stable/stock/IBM/financials/2?token=Tsk_974c2b98c67e47f5b92bd7d6cfe869c0&period=annual
                full_url = url + "/stable/stock/" + form.ticker.data + "/" + f + "/" + form.years_behind.data + \
                           "?token=" + token + "&period" + "=annual"
                # make the request
                s = requests.Session()
                r = s.get(full_url)

                json_data = json.loads(r.text)

                # don't show the following data
                dont_display = ['currency', 'fiscalDate', 'reportDate']

                # remove non alphanumeric characters (url has balance-sheet, but the JSON has balancesheet)
                f = re.sub(r'\W+', '', f)
                for i in range(int(form.years_behind.data)):
                    # getting only the year
                    full_date = json_data[f][i]["fiscalDate"]
                    short_date = full_date.split('-')[0]
                    for k, v in json_data[f][i].items():
                        if k not in dont_display:
                            new_record = Ticker(stock=form.ticker.data, key=k, value=v, fy=short_date)
                            db.session.add(new_record)
            db.session.commit()

        return render_template('home.html', title='Financials', form=form, ticker=ticker)
    elif request.method == 'GET':
        ticker = Ticker.query.all()
    return render_template('home.html', title='Financials', form=form, ticker=ticker)
