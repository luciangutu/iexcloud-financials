from flask import render_template, url_for, flash, redirect, request
from financials import app, db
from financials.forms import HomeForm
from financials.models import Ticker


@app.route('/', methods=['GET', 'POST'])
def home():
    form = HomeForm()
    if form.validate_on_submit():
        # ticker = Ticker.query.get_or_404(form.ticker.data)
        ticker = Ticker.query.all()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        ticker = Ticker.query.all()
    return render_template('home.html', title='Financials', form=form, ticker=ticker)
