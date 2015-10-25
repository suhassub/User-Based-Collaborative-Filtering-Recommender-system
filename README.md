# User-Based-Collaborative-Filtering-Recommender-system
Implements a simple user-based collaborative filtering recommender system for predicting the ratings of an item using the data given. The prediction would be done using k nearest neighbors and Pearson Correlation.  Finally using the similarity of the k nearest neighbors, predict the ratings of the new item for the given user


Format of ratings file
-------------------------
 The input file consists of one rating event per line. Each rating event is of the form:
user_id\trating\tmovie_title
 The user_id is a string that contains only alphanumeric characters and hyphens and spaces (no tabs).
 The rating is one of the float values 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, and 5.0.
 The movie_title is a string that may contain space characters (to separate the words).
 The three fields -- user_id, rating, and the movie_title -- are separated by a single tab character (\t).


Input
------
python Subramanya_Suhas_collabFilter.py ratings-dataset.tsv Kluver ‘The Fugitive’ 10

ratings-dataset.tsv: input file
Kluver: User id
Movie: The Fugitive
K: 10


The program will output:
-------------------------
 K nearest neighbors with their user ids and similarity values separated by space as per the output
file
 Rating prediction for item.



Sample Ratings File - ratings-dataset.tsv
-----------------------------------------
The file is uploaded to the github
