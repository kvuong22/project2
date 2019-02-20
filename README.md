# **README**

## **Definitions for Functions in movies_tools.py**
movies_tools.py contains the class Movie, which contains the functions needed to generate the list of the 10 movies and their respective IMDB ratings extracted from the movies_clean.csv file. It also contains the code that counts the total number of movies available in movies_clean.csv.

## **Relationship between movies_tools.py and SI507_project2.py**
SI507_project2.py imports all of the code from movies_tools.py and utilizes the Flask module to use the code in a Flask application, viewable via web browser and can be tested through a web browser.



## **Project Dependencies**

This project requires installation of what is listed in the requirements.txt file to run the project.



## **Running Flask Application**

To run the Flask application, in the command prompt, run 'python SI507_project2.py runserver'. Access the webpage either by using 1) the generated URL in the command prompt or by using the URL link 2) http://localhost:5000 and paste it into the browser. The home page should have a message saying, "3145 movies recorded."

### **Accessing the Movie Titles and Ratings Route**
To access the route to the movie titles and ratings, edit the URL parameters in the browser to include '/movies/ratings'. A list of 10 movies and their respective IMDB ratings will be shown on the webpage.
