import sqlite3

#connect to database test
conn = sqlite3.connect('rattrapage.db')

#create cursor
c = conn.cursor()

#create table
c.execute("SELECT * FROM ping_request_results")


print(c.fetchall())

#Commit our command
conn.commit()

#close connection
conn.close()