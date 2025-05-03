from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from better_profanity import profanity


class Message(db.Model):
    __tablename__ = "messages"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    message_body = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False
    )
    time_stamp = db.Column(db.Date, default=date.today())

    user = db.relationship("User", back_populates="messages")

    @property
    def message(self):
        return self.message_body

    @message.setter
    def message(self, txt):
        self.message_body = self.check_message(txt)

    def check_message(self, message):
        profanity.load_censor_words()
        censored_text = profanity.censor(message)
        return censored_text

    def to_dict(self):
        return {"id": self.id, "message": self.message_body, "date": self.time_stamp}
