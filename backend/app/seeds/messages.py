from app.models import db, User, environment, SCHEMA, Message
from sqlalchemy.sql import text


def seed_messages():
    msg1 = Message(
        message="hello world",
        user_id=1,
    )
    msg2 = Message(
        message="web sockets",
        user_id=1,
    )
    msg3 = Message(
        message="Hey Demo",
        user_id=2,
    )
    messages = [msg1, msg2, msg3]
    for message in messages:
        db.session.add(message)

    db.session.commit()


def undo_messages():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.messages RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute(text("DELETE FROM messages"))

    db.session.commit()
