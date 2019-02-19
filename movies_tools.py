import csv
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)


class Movie:
    def __init__(self, movie_lst):
        self.title = movie_lst[0]
        self.rating = movie_lst[14]

    def __str__(self):
        return '{} | {}'.format(self.title,self.rating)

moviefile = open('movies_clean.csv', 'r', encoding ='utf-8')
row_reader = csv.reader(moviefile)
header = next(row_reader)

movie_rating_lst = []
for row in row_reader:
    movie_rating_lst.append(row)

row_count = sum(1 for row in movie_rating_lst)
print(row_count)


for movie in movie_rating_lst:
    m = Movie(movie)

# print(m)



# define a class Movie that accepts as constructor input one row of the movies_clean.csv file (in whatever format you think is appropriate for you).
#
# That class should have any instance variables and/or method(s) you think will be useful for building your Flask app, and at least one of your Flask app's routes should create instances of that class.
#
# We suggest that you make this plan based on your goals for the Flask app (detailed below), and go back and forth between the two Python files making plans as you write code (similarly to how you might have gone back and forth between your lab3_code.py and your SI507_project1.py code to work on Project 1!). We expect you to use instances of this class in the Flask app.
#
# It is also possible that you will choose to define additional function/s in movies_tools.py and invoke them in the Flask code, but it is not necessary to do so. You can make your own design decisions here.
#
# We also suggest that, as you work, you have, beneath an if __name__ == "__main__": statement, code that opens up the clean movies data file and uses its contents to test out some instances of this class -- in order to ensure it works as you want it to. It's more annoying to debug inside Flask than it is to debug code outside Flask first, so read what your goals are, make sure your class works, and THEN integrate it into the app!
#
#
