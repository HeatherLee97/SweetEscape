from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import Message, db
from ..forms.message_form import MessageForm

message_routes = Blueprint("messages", __name__)


@message_routes.route("/")
# @login_required
def get_messages():
    """
    Query all the messages and return them
    """
    messages = Message.query.all()
    rev_messages = reversed(messages)
    return {"messages": [message.to_dict() for message in rev_messages]}


@message_routes.route("/", methods=["POST"])
# @login_required
def post_message():
    form = MessageForm()
    print(request.get_json())

    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        data = form.data
        print(data)
        message = Message(message=form.data["message"], user_id=form.data["user_id"])

        db.session.add(message)
        db.session.commit()
        return {"Message": message.to_dict()}
    else:
        return form.errors, 401
