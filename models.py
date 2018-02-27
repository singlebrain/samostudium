import sqlite3 as sql

def insertUser(username,password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

def retrieveUsers():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM users")
	users = cur.fetchall()
	con.close()
	return users
def userdetail(username):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM users WHERE username=%02s")%username
	user = cur.fetchall()
	con.close()
	return user

def useralldetail(username):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM users WHERE username=%02s")%username
	user = cur.fetchall()
	con.close()
	return user

