from flask import Flask
from movies_tools import *

app = Flask(__name__)



@app.route('/')
def home():
    return '<h1> {} movies recorded.</h1>'.format(row_count)

# @app.route('/movies/ratings')
# def function():
#     pass

# Movie Title | IMBD rating
#
# 	e.g. (this is an example that shows just the first FOUR movies in the dataset in the original order)
#
# 	The Land Girls | 6.1
# 	First Love, Last Rites | 6.9
# 	I Married a Strange Person | 6.8
# 	Let's Talk About Sex | NA


# Each of these two routes should depend upon the existence of movies_clean.csv. We expect you to include in your directory the CSV file you already created in HW4.
#
# Your app should work regardless of what data is in a movies_clean.csv file -- as long as that file is in exactly the same format, with the same expectations, as the one that you created in HW4. (e.g. maybe another movies_clean.csv could have different movies listed, but the basic information that each has would still be the same, dates would be formatted in the same way, any missing data would still have "NA" in its place)
#
# N.B. When you submit this project, you should include your movies_clean.csv file in the GitHub repo as well as any code files you need, of course.

if __name__ == '__main__':
    app.run()
