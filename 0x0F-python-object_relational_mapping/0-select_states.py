#!/usr/bin/python3
""" a script to list all database state field"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    hst = "localhost"
    prt = 3306
    usr = arv[1]
    pas = argv[2]
    dbs = argv[3]
    db = MySQLdb.connect(host=hst, port=prt, user=usr, passwd=pas, db=dbs)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for r in rows:
        print(r)
        cursor.close()
        db.close()
