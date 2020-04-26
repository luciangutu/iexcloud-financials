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
import datetime
from financials.models import Ticker
db.create_all()
```
Add some demo data manually:
```
stock = Ticker(stock='FB', key='test', value='200', fy='2019')
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

SQLite queries:
```
$ sqlite3
sqlite> .open financials/financials.db
sqlite> .tables
ticker
sqlite> .schema ticker
CREATE TABLE ticker (
	id INTEGER NOT NULL, 
	stock VARCHAR(5) NOT NULL, 
	"key" VARCHAR(120) NOT NULL, 
	value INTEGER NOT NULL, 
	date_posted DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL, 
	fy VARCHAR(4) NOT NULL, 
	PRIMARY KEY (id)
);
sqlite> select * from ticker;
1|FB|test|200|2020-04-26 17:06:34|2019
```

Clean the SQLite DB:
```
db.drop_all()
```

## Run the project:
```
python run.py
```
Then browse:
http://127.0.0.1:5000/ 


TODO:
- drop DB or a mechanism to update the DB for each ticker
- UX
- add P/E ratio and EPS from API to the DB or UX
