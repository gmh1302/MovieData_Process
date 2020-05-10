# app.py
# pip install flask
# pip install flask-mysql

from flask import *
from models import score_compare, comment_word_analysis

import math

app = Flask(__name__)


# http://127.0.0.1:5000/
@app.route("/")
def home():
    return render_template('home.html')

# http://127.0.0.1:5000/score
@app.route("/score")
def score():
    after_val = score_compare.select_after_data()
    before_val = score_compare.select_before_data()

    return render_template('score.html', after_avg_val = after_val, before_avg_val = before_val)

 # http://127.0.0.1:5000/comment
@app.route("/comment")
def comment():
    return render_template('comment.html')   

if __name__ == '__main__':

    app.debug = True
    app.run()
