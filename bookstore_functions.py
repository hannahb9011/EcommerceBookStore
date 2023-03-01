# Hannah Bradley 
# Mar 1 2023
# 
# This script holds all the functions used to recieve results for the application.
# Using sqlite, queries are able to be written to recieve the output being searched for


import os
import sqlite3

dirname = os.path.dirname(__file__) #get path of this directory
connection = sqlite3.connect(dirname + "/bookstore.db") #connect to database 
cur = connection.cursor() #allows for querying and returning results

def test():
    result = cur.execute("select ISBN from books")
    return result.fetchall()

t = test()
for val in t:
    print(val[0])
