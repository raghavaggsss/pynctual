#!/usr/bin/env python

import sqlite3

def createdb():

    try:
        db = sqlite3.connect('db')

        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY AUTOINCREMENT, rollno INTEGER NOT NULL, filename TEXT)''')

    except Exception as e:
        db.rollback()
        raise e 
    
    finally:
        db.close()


def updatedb(roll_no):
    roll_no = int(roll_no)

    try:
        global conn
        db = sqlite3.connect("db")
        _cursor = db.cursor()

        # Ensure that entry should not exist already
        for row in _cursor.execute("SELECT rollno FROM person"):
            if row[0] == roll_no:
                print("Entry already exist")
                return
            else:
                pass

        # Ensure xyt file of intern with "rollno: 000" is named as 000.xyt
        filename = str(roll_no)+'.xyt'
        if(_cursor):
            _cursor.execute('''INSERT INTO person (rollno, filename) VALUES(?,?)''', (roll_no, filename))
        else:
            raise Exception("_cursor is NULL")

        db.commit()

    except Exception as e:
        db.rollback()
        raise e

    finally:
        db.close()


def displaydb():
    try:
        db = sqlite3.connect("db")
        _cursor = db.cursor()
        _rows = _cursor.execute("SELECT id, rollno, filename from person")

        for row in _rows:
            print('ID: {} ROLL-NO: {} FILENAME: {}'.format(row[0], row[1], row[2])) 

    except Exception as e:
        db.rollback()
        raise e
    
    finally:
        db.close()
