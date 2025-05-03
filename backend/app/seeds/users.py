from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    users = [
        User(username="johnsmith", email="john.smith@example.com", password="password"),
        User(username="emilywong", email="emily.wong@example.com", password="password"),
        User(username="davidlee", email="david.lee@example.com", password="password"),
        User(
            username="kayla.park", email="kayla.park@example.com", password="password"
        ),
        User(username="jen.wong", email="jen.wong@example.com", password="password"),
        User(username="alex.hall", email="alex.hall@example.com", password="password"),
        User(
            username="sophia.kim", email="sophia.kim@example.com", password="password"
        ),
        User(
            username="natalie.patel",
            email="natalie.patel@example.com",
            password="password",
        ),
    ]
    for user in users:
        db.session.add(user)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
