import sqlite3

#connect to database test
conn = sqlite3.connect('rattrapage.db')

#create cursor
c = conn.cursor()

#create table
c.execute("INSERT INTO ping_request_results VALUES ('TimeStamp','1.1.1.1','Nom de domaine','Ceci est une description',0.45,1)")

print("Values insert sucessfuly")

#Commit our command
conn.commit()

#close connection
conn.close()