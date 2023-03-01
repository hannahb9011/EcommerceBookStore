# Hannah Bradley 
# Feb 27 2023
# 
# This script is used to take in the information from the cvs that are saved in the books_data folder.
# They are read into DataFrame so that they can be easily entered into a sqlite database that will be used
# in the rest of this project

import os
import sqlite3
import pandas as pd

#create variables that will give the paths to different files
dirname = os.path.dirname(__file__) #get path of this directory
books = "/books_data/books.csv"
ratings = "/books_data/ratings.csv"
users = "/books_data/users.csv"

#take in data from csv and create a DataFrame with it
df_books = pd.read_csv(dirname + books, sep=';', on_bad_lines='skip', encoding='latin-1')
df_ratings = pd.read_csv(dirname + ratings, sep=';', on_bad_lines='skip', encoding='latin-1')
df_users = pd.read_csv(dirname + users, sep=';', on_bad_lines='skip', encoding='latin-1')
#print(df_ratings.head(50))

connection = sqlite3.connect(dirname + "/bookstore.db") #create/connect to database 
try:
    #create table for each data file using the DataFrames
    df_books.to_sql('books', connection, if_exists="fail") 
    df_ratings.to_sql('ratings', connection, if_exists="fail") 
    df_users.to_sql('users', connection, if_exists="fail") 
except ValueError: #Error check that the table doesnt already exist. Check is done because of the 'if_exist' parameter
    print("\nA table under that name is already in the database")