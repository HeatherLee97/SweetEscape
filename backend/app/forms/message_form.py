from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from app.models import User, Message


def valid_user(form, field):
    user_id = form.data["user_id"]
    user = User.query.filter(User.id == user_id).first()
    if not user:
        raise ValidationError("Invalid User")


class MessageForm(FlaskForm):
    message = StringField("Message", validators=[DataRequired()])
    user_id = IntegerField("User Id", validators=[DataRequired(), valid_user])
    date = DateField("Date")
