from flask import Flask, request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/posts/')
def posts():
    con = sql.connect("posts.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from post")
    res = {}
    rows = cur.fetchall()

    index = 0
    for entry in rows:
        res[index] = dict(entry)
        index += 1
    return {"rows": res}


@app.route('/posts/create/')
def create():
    title = request.args.get('title')
    text = request.args.get('text')
    with sql.connect("posts.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO post (title,text) VALUES(?, ?)", (title, text))

        con.commit()
    return {"title": title, "text": text}


if __name__ == '__main__':
    app.run()
