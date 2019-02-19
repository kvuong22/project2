from flask import Flask
from movies_clean import *
# Each of these two routes should depend upon the existence of movies_clean.csv. We expect you to include in your directory the CSV file you already created in HW4.
#
# Your app should work regardless of what data is in a movies_clean.csv file -- as long as that file is in exactly the same format, with the same expectations, as the one that you created in HW4. (e.g. maybe another movies_clean.csv could have different movies listed, but the basic information that each has would still be the same, dates would be formatted in the same way, any missing data would still have "NA" in its place)
#
# N.B. When you submit this project, you should include your movies_clean.csv file in the GitHub repo as well as any code files you need, of course.
