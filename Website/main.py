from flask import Flask
from flask import render_template
from flask import request
import datetime
from operator import itemgetter
import sqlite3
app = Flask(__name__)


@app.route('/')
def main():
    # conn = get_db_connection()
    # data = conn.execute('SELECT message FROM server_one_logs').fetchall()
    # conn.close()
    return render_template('index.html')

@app.route('/query/', methods=["POST"])
def query():
    want=request.form.get('want')
    att=request.form.getlist('attachment')
    timestamp=request.form.getlist('timestamp')
    mid=request.form.getlist('messageID')
    guild=request.form.getlist('guild')
    channel=request.form.getlist('channelID')
    conn=get_db_connection()
    sql1="""SELECT author,message """
    sql2="""FROM server_one_logs WHERE message LIKE ?"""
    if att:
        sql1+=""",attachment """
    if mid:
        sql1+=""",messageID """
    if channel:
        sql1+=""",channel """
    if guild:
        sql1+=""",guild """
    if timestamp:
        if timestamp[0]=="epoch":
            sql1+=""",timestamp """
        elif timestamp[0]=="date":
            sql1+=""",DATETIME(timestamp,'unixepoch', 'localtime') """
    # print(sql1,timestamp)
    sql=sql1+sql2
    data=conn.execute(sql,('%'+want+'%',)).fetchall()
    conn.close()
    if want=="":
        return render_template('index.html')
    return render_template('index.html',data=data)

def get_db_connection():
    conn = sqlite3.connect('logs.db')
    return conn

if __name__ == "__main__":
    app.run(debug=True)