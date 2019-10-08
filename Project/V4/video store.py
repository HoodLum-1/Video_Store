"""	Author: Malesela Sithole
	Date: 15/04/2017
	Title: video_store
	Purpose: To store data for customers and movies of the video store
"""
import mysql.connector
from mysql.connector import errorcode

try:
	conn = mysql.connector.connect(
	user='root',
	password='MySQL',
	host='localhost'
	)
	
#Drop database if database exists	
	cur = conn.cursor()
	cur.execute("DROP DATABASE IF EXISTS video_store;")
	print("Database video_store dropped")
	cur.close()
	
#Create database called video_store
	cur = conn.cursor()
	cur.execute("CREATE DATABASE video_store;")
	print("Database video_store created")
	cur.close()

#Change database to database video_store
	cur = conn.cursor()
	cur.execute("USE video_store;")
	print("using database video_store")
	print()
	cur.close()
	
#Drop table if exists 	
	cur = conn.cursor()
	cur.execute("DROP TABLE IF EXISTS customers;")
	print("Table customer Dropped")
	cur.close()
#Drop table if exists 
	cur = conn.cursor()
	cur.execute("DROP TABLE IF EXISTS videos;")
	print("Table videos Dropped")
	cur.close()
#Drop table if exists 
	cur = conn.cursor()
	cur.execute("DROP TABLE IF EXISTS hire;")
	print("Table hire Dropped")
	print()
	cur.close()

#Create table customers
	cur = conn.cursor()
	cur.execute("""
			CREATE TABLE customers
			(
				custId INT NOT NULL AUTO_INCREMENT, 
				fname VARCHAR(40) NOT NULL,
				sname VARCHAR(40) NOT NULL,
				address VARCHAR(40) NOT NULL,
				phone VARCHAR(10) NOT NULL UNIQUE,
				PRIMARY KEY(custId)
			);
	
	""") #Check syntax for auto increment
	cur.close()
	conn.commit()
	print("Table customers created successfully")
	cur.close()
	
#Create table videos
	cur = conn.cursor()
	cur.execute("""
			CREATE TABLE videos
			(
				videoId INT NOT NULL,
				videoVer INT NOT NULL,
				vname VARCHAR(15) NOT NULL,
				type VARCHAR(1) NOT NULL,
				dateAdded DATE NOT NULL
			);
	
	""")
	cur.close()
	conn.commit()
	print("Table videos created successfully")
	cur.close()
	
#Create table hire
	cur = conn.cursor()
	cur.execute("""
			CREATE TABLE hire
			(
				custId INT NOT NULL,
				videoId INT NOT NULL,
				videoVer INT NOT NULL,
				dateHired DATE NOT NULL,
				dateReturn DATE
			);
	
	""")
	cur.close()
	conn.commit()
	print("Table hire created successfully")
	cur.close()

#Hnadle exceptions that may occur	
except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Incorrect user name or password!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
        else:
                print(err)

#End of file video_store
