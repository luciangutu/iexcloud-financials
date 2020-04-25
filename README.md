# iexcloud-financials
## Setup:

Requirements:
```
pip install flash flask-sqlalchemy flask-wtf sqlalchemy
```

Create credential file:
```
url = 'https://sandbox.iexapis.com'
token = 'Tsk_[...]'
```

Create the SQLite DB:
```
from financials import db
from datetime import datetime
from financials.models import Ticker
db.create.all()
```
Add some demo data manually:
```
stock = Ticker(stock='C', key='test', value='200', date_posted=datetime(2019, 10, 10, 10, 10), fy='2019')
db.session.add(stock)
db.session.commit()
```
Some test queries:
```
Ticker.query.all()
Ticker.query.first()
Ticker.query.filter_by(stock='FB').all()
Ticker.query.filter_by(stock='FB').first()

fb = Ticker.query.filter_by(stock='FB').first()
fb.id
fb.date_posted

Ticker.query.get(1)
```

Clean the SQLite DB:
```
db.drop_all()
```

## Run the proj:
```
python run.py
```
Then browse:
http://127.0.0.1:5000/ 


I've learn some Flask from here:
https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog
