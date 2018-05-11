from flask import Flask, render_template, request
import records
#from database import *

app = Flask(__name__)

@app.route('/')
def index():
    db = records.Database('sqlite:///movie_data.db')
    res = db.query('SELECT title FROM movies LIMIT 10')

    return render_template('index.html', res=res)


if __name__ == '__main__':
    app.run(debug=True)