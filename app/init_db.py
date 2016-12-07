# Reference followed - https://www.youtube.com/watch?v=fnJhWmlFdUw&index=10&list=LLK10Iddlp2ensam01EEGKHQ
import sqlite3
from flask import Flask

app=Flask(__name__)

# the name of the database
DATABASE = "myapp.db"

def init_db():
    db = sqlite3.connect(DATABASE)

    with app.open_resource("db.sql", mode="r") as f: # mode = r means read only
    sql = f.read()

    print(sql) # prints sqlite3
    db.cursor().execute(sql) # runs statement
    db.commit() # allows to save info
    db.close() # close database

    # Runs
    if __name__ == "__main__":
        init_db()