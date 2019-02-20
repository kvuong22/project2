from flask import Flask
from movies_tools import *

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1> {} movies recorded.</h1>'.format(row_count)


@app.route('/movies/ratings')
def movie_rating():
    mr_string = ''
    for item in movie_insts:
        mr_string += item.__str__() + '<br>'
    return mr_string


if __name__ == '__main__':
    app.run()
