from wtforms import Form, StringField, FloatField, validators, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class FlowerForm(FlaskForm):
    sepal_length = FloatField('Sepal Length', validators=[DataRequired()])
    sepal_width = FloatField('Sepal Width', validators=[DataRequired()])
    petal_length = FloatField('Petal Length', validators=[DataRequired()])
    petal_width = FloatField('Petal Width', validators=[DataRequired()])

    submit = SubmitField("Analyse Flower")