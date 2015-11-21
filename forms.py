from flask_wtf import Form
from wtforms import TextField, IntegerField, StringField, SelectField, DateField, TextAreaField, SubmitField, BooleanField, validators
from wtforms.validators import Required, DataRequired, ValidationError

class ContactForm(Form):
    email = TextField('E-mail', [validators.DataRequired("Enter a valid email address"), validators.Email("Enter a valid email address")])
    subject = TextField('Subject', [validators.DataRequired("What's the nature of your message?")])
    message = TextAreaField('Message', [validators.DataRequired("Didn't you want to say something?")])
    submit = SubmitField('Send')

