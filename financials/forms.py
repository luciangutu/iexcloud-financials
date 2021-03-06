from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError


class HomeForm(FlaskForm):
    ticker = StringField('Ticker', validators=[DataRequired(), Length(min=1, max=5)])
    years_behind = StringField('Years of data')
    submit = SubmitField('Get!')
    update = SubmitField('Update Data')
