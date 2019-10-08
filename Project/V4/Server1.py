"""	Author: Malesela Sithole
	Date: 15/04/2017
	Title: server
	Purpose: To process client requests and return the results to the client for output
"""

#Server.py

#Import of the neccesary modules
import mysql.connector, socket
from mysql.connector import errorcode
import sys, traceback
from time import strftime

#Creation of the Server class
class Server:
        def __init__(self,port,
        #Construct the instance of the server
                listen = 6,
                timeout = 10,
                buf = 4096,
                queueSize = 10):

                self.port = port
                self.soc = socket.socket(socket.AF_INET,        #Create TCP socket
                        socket.SOCK_STREAM)
                self.listen = listen
                self.timeout = timeout
                self.bufsize = buf

        def send(self, conn, string):
                #Override the send function
                conn.send(bytes(string,encoding="ascii"))

        def recv(self, conn):
                #Indicates how many bytes can=n be recived from client
                return str(conn.recv(self.bufsize),encoding="ascii")
        
        def videostore():
                try:
                        conn = mysql.connector.connect(user='root',
                                                       password='password',
                                                       host='localhost',
                                                       database='video_store')
                except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                                print("Incorrect user name or password!")
                        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                                print("Database does not exist")
                        else:
                                print(err)

        #def reg():
        def run(self):
                #Runs the server
                print("Server started...\nport:",self.port,
                      "\nlisten number:",self.listen)
                print()
                #Make port available for client to connect
                self.soc.bind(('',self.port))
                self.soc.listen(self.listen)

                while True:
                        c, addr = self.soc.accept() #Accept connection
                        print("Client connected")
                        Cho = self.recv(c)
                        print('Recived option', Cho)
                        print()
                        
                        #Processing option 1
                        if Cho == '1':
                                print('Option 1 choosen')
                                phone = self.recv(c)
                                print(phone)



                                #Try statement to handling any errors with the database
                                try:
                                        conn = mysql.connector.connect(user='root',
                                                               password='password',
                                                               host='localhost',
                                                               database='video_store')
                                        
                                        #Inserting customer data into database video_store
                                        #Try statement rollback if theres an error
                                        try:
                                                cur = conn.cursor()
                                                cur.execute("SELECT * FROM customers WHERE phone = %s" % (phone))
                                                data = cur.fetchall()
                                                msgNF = 'Phone does not exits, you may continue to register'
                                                msgF = 'Found'
                                                if not data:
                                                        print('Phone Number not found')
                                                        c.send(msgNF.encode('ascii'))
                                                        fname = self.recv(c)
                                                        print(fname)
                                                        sname = self.recv(c)
                                                        print(sname)
                                                        address = self.recv(c)
                                                        print(address)

                                                        dart = "INSERT INTO customers (fname, sname, address, phone)VALUES(%s, %s, %s, %s)"
                                                        cur.execute(dart, (fname, sname, address, phone))
                                                        print("Number of rows inserted: %d" % cur.rowcount)
                                                        cur.close()
                                                        conn.commit()
                                                        #conn.close()
                                                        print()
                                                        print("Customer registered successfully")
                                                        c.send('Customer registered successfully'.encode('ascii'))
                                                else:
                                                        print ('Found')
                                                        c.send(msgF.encode('ascii'))
                                        except:
                                                conn.rollback()
                                                print("Error: Inserting data into database")
                                                
                                except mysql.connector.Error as err:
                                        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                                                print("Incorrect user name or password!")
                                        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                                                print("Database does not exist")
                                        else:
                                                print(err)
                                                continue
                                        
                        #Processing option 2
                        elif Cho == '2':
                                print('Option 2 choosen')
                                #videoVer = self.recv(c)
                                #print(videoVer)
                                #videoVer = int(videoVer)
                                mName = self.recv(c)
                                print(mName)
                                vtype = self.recv(c)
                                print(vtype)
                                dateAdded = strftime("%Y-%m-%d")
                                print(str(dateAdded))
                                #videoId = 'Hello'
                                videoVer = 1

                                #Try statement to handling any errors with the database
                                try:
                                      conn = mysql.connector.connect(user='root',
                                                               password='password',
                                                               host='localhost',
                                                               database='video_store')

                                      try:
                                              #Try statement rollback if theres an error
                                              cur = conn.cursor()
                                              cur.execute("SELECT * FROM videos")
                                              data = cur.fetchall()

                                              if data != mName:
                                                      for row in data:
                                                              videoId = row[0]
                                                              print(videoId)
                                                              videoId = int(videoId + 1)
                                                      
                                                      inc = "INSERT INTO videos ( videoId, videoVer, vname, type, dateAdded)VALUES(%s, %s, %s, %s, %s)"
                                                      cur.execute(inc, (videoId, videoVer, mName, vtype, dateAdded))
                                                      
                                                      print("Number of rows inserted: %d" % cur.rowcount)
                                                      cur.close()
                                                      conn.commit()
                                                      #conn.close()
                                                      
                                                      print("Movie registered successfully")
                                                      c.send('Movie registered successfully'.encode('ascii'))
                                              else:
                                                      for row in data:
                                                              videoVer = row[1]
                                                              print(videoVer)
                                                              videoVer = int(videoVer + 1)
                                                              
                                                      inc = "INSERT INTO videos ( videoId, videoVer, vname, type, dateAdded)VALUES(%s, %s, %s, %s, %s)"
                                                      cur.execute(inc, (videoId, videoVer, mName, vtype, dateAdded))

                                                      print("Number of rows inserted: %d" % cur.rowcount)
                                                      cur.close()
                                                      conn.commit()
                                                      #conn.close()
                                                      
                                                      print("Movie registered successfully")
                                                      c.send('Movie registered successfully'.encode('ascii'))
                                                        
                                      except:
                                               conn.rollback()
                                               print("Error: Inserting data into database")
                                               c.send('Movie NOT registered successfully'.encode('ascii'))
                                               
                                except mysql.connector.Error as err:
                                        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                                                print("Incorrect user name or password!")
                                        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                                                print("Database does not exist")
                                        else:
                                                print(err)
                                                continue
                                                
                        #Processing option 3        
                        elif Cho == '3':
                                print('Option 3 choosen')
                                phone = self.recv(c)
                                print(phone)
                                videoId = self.recv(c)
                                print(videoId)
                                dateHired = strftime("%Y-%m-%d")

                                #Try statement to handling any errors with the database
                                try:
                                        conn = mysql.connector.connect(user='root',
                                                               password='password',
                                                               host='localhost',
                                                               database='video_store')
                                        
                                        #retriving customer data from database video_store
                                        cur = conn.cursor()
                                        cur.execute ("SELECT * FROM customers WHERE phone = %s" % (phone))
                                        phone_result = cur.fetchall()
                                        if not phone_result:
                                                print('Phone not found')
                                                MKG = 'Phone not found'
                                                c.send(MKG.encode('ascii'))
                                        else:
                                                       cur.execute ("SELECT * FROM videos WHERE videoId = %s" % (videoId))

                                                       result_set = cur.fetchall()
                                                       print ('Fecthing data')

                                                       if not result_set:
                                                               print('videoId not found')
                                                               MSG = 'videoId not Found, You can not hire if not registered'
                                                               c.send(MSG.encode('ascii'))
                                                       else:
                                                               query = "INSERT INTO hire "
                                                               query += "SELECT videoId, videoVer, dateHired FROM videos "
                                                               query += "WHERE videoId = " + videoId
                                                               custId = "SELECT * FROM customers WHERE phone = %s" % phone
                                                               videoVer = "SELECT videoVer FROM videos WHERE videoId = %s" % videoId
                                                               cur.execute(query, (custId, videoId, videoVer, dateHired))

                                                               print("Number of rows inserted: %d" % cur.rowcount)
                                except mysql.connector.Error as err:
                                        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                                                print("Incorrect user name or password!")
                                        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                                                print("Database does not exist")
                                        else:
                                                print(err)
                                                continue
                                                
                        #Processing Option 4
                        elif Cho == '4':
                                print('Option 4 choosen')
                                videoId = self.recv(c)
                                print(videoId)
                                returndate = strftime("%Y-%m-%d")
                                print(returndate)

                                #Try statement to handling any errors with the database
                                try:
                                        conn = mysql.connector.connect(user='root',
                                                               password='password',
                                                               host='localhost',
                                                               database='video_store')
                                        
                                        #retriving customer data from database video_store
                                        cur = conn.cursor()
                                        #try:
                                        query = "UPDATE hire SET "
                                        query += "hire.dateReturn=%s " % returndate
                                        query += "WHERE hire.videoId='%s'"  % videoId

                                        cur.execute(query)

                                        result_set = cur.fetchall()
                                        print('Fetching Results')
                                                
                                        if not result_set:
                                                print('Movie not found')
                                                MKG = 'Movie not found'
                                                c.send(MKG.encode('ascii'))
                                        else:

                                                print("%s date returned: " % (returndate))
                                                print()
                                                print("Updated successfully")
                                                c.send('Movie returned successfully'.encode('ascii'))

                                        #except:
                                                #print("Error: Unable to update table hire")

                                        cur.close()
                                        conn.commit()
                                        #conn.close()
                                
                                except mysql.connector.Error as err:
                                        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                                                print("Incorrect user name or password!")
                                        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                                                print("Database does not exist")
                                        else:
                                                print(err)
                                                continue
  
                        #The server checks for invaild input
                        #The server exits if option x is choosen
                        elif Cho == 'x':
                                sys.exit(0)
                        else:
                                print('Invalid input')
                                c.send('Invalid option selected'.encode('ascii'))
                                continue

if __name__ == "__main__":
        s = Server(8081, listen = 1000)
        s.run()
