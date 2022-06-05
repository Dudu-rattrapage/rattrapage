import sqlite3

# connect to database test
conn = sqlite3.connect('rattrapage.db')

# create cursor
c = conn.cursor()

# create table
c.execute('''CREATE TABLE IF NOT EXISTS ping_request_results (
    Timestamp text,
    Ip text,
    Domain text,
    Description text,
    Ping real,
    PacketLoss integer
)''')

# Datatypes : NULL, INTEGER, REAL, TEXT, BLOB

# Commit our command
conn.commit()

# close connection
conn.close()


def initialize_db_tables():
    # connect to database test
    conn = sqlite3.connect('rattrapage.db')

    # create cursor
    c = conn.cursor()

    # create table
    # Timestamp DATETIME default CURRENT_TIMESTAMP not null,
    c.execute('''CREATE TABLE IF NOT EXISTS ping_request_results (
        Timestamp text,
        Ip text,
        Domain text,
        Description text,
        Ping real,
        PacketLoss integer
    )''')

    # Datatypes : NULL, INTEGER, REAL, TEXT, BLOB

    # Commit our command
    conn.commit()

    # close connection
    conn.close()

def reset_database():
    # connect to database test
    conn = sqlite3.connect('rattrapage.db')

    # create cursor
    c = conn.cursor()

    # create table
    c.execute('''DROP TABLE ping_request_results''')

    # Datatypes : NULL, INTEGER, REAL, TEXT, BLOB

    # Commit our command
    conn.commit()

    # close connection
    conn.close()