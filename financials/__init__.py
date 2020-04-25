from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '242db1cea8760fc987c57435efbebbc6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///financials.db'
db = SQLAlchemy(app)

from financials import routes
