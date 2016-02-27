import sqlite3 as db
import sqlite3
from weather import RainEventMsg
print(sqlite3.sqlite_version)
def get_data():
    conn = db.connect(':memory:')
    cur = conn.cursor()

    cur.execute("CREATE TABLE dailyTemps(month TEXT, day TEXT, high REAL, low REAL)")
    cur.execute("CREATE TABLE rainEvents(month TEXT, day TEXT, amount REAL)")
    cur.execute("CREATE TABLE countyPopulation(county TEXT, year REAL, pop REAL)")

    cur.execute("""INSERT INTO countyPopulation(county, year, pop) VALUES ('Hall', 1980, 2350),
                                                       ('Hall', 1990, 4000),
                                                       ('Hall', 2000, 5120),
                                                       ('Hall', 2010, 5130),
                                                       ('Franklin', 1980, 1350),
                                                       ('Franklin', 1990, 5340),
                                                       ('Franklin', 2000, 9530),
                                                       ('Franklin', 2010, 1000);""")

    cur.execute("""INSERT INTO rainEvents VALUES('March', 27, 1.5),
                                                ('March', 28, 1.9)
                """)


    cur.execute("""INSERT INTO dailyTemps VALUES('March', 27, 20, 30),
                                                ('March', 28, 22, 30),
                                                ('March', 29, 22, 31)
                """)
    conn.commit()
    return cur