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
# print(row_count)

movie_insts = []
for movie in movie_rating_lst[:10]:
    m = Movie(movie)
    movie_insts.append(m)

# print(movie_insts)
