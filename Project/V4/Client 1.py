"""	Author: Malesela Sithole
	Date: 15/04/2017
	Title: client
	Purpose: To allow user input, and communication with the server.
"""
##client.py

#Import of the neccesary modules
import socket

#Creation of the Client class
class Client:
        def __init__(self,
                host,
                port,
                bufsize = 1024,
                timeout = 10):

                self.client =socket.socket(socket.AF_INET,
                                socket.SOCK_STREAM)
                self.host = host
                self.port = port
                self.bufsize = bufsize
                self.timeout = timeout

        def connect(self):
                self.client.connect((self.host,self.port))
                print('Client connected to server')
        
        def close(self):
                self.client.close()

        def send(self, string):
                self.client.send(bytes(string,"ascii"))

        def recv(self):
                return str(self.client.recv(self.bufsize),
                           encoding="ascii")

if __name__ == "__main__":
        #Connects the to the server
        c = Client('localhost',8081)
        c.connect()

        #Client Menu print out
        print("=================================")
        print("|        VIDEO STORE		|")
        print("=================================")
        print("| 1. Register Customer		|")
        print("| 2. Register Movie		|")
        print("=================================")
        print("| 3. Hire Out Movie		|")
        print("| 4. Return Movie		|")
        print("=================================")
        print("| x. Exit			|")
        print("=================================")

        #c.send(Cho)

        #server_reply = c.recv()
        #print()
        #print('server reply:', server_reply)

        while True:
                try:
                        Cho = str(input('Choice:'))
                        
                        c.send(Cho)
                        
                        #server_reply = c.recv()

                        if Cho == '1':
                                print('Register customer')
                                print()
                                phone = str(input('Enter phone:'))
                                c.send(phone)
                                msg = c.recv()
                                if msg == 'Phone does not exits, you may continue to register':
                                        print(msg)
                                        print('Enter the following:')
                                        print()
                                        #Ask user for the rest of their data
                                        fname = str(input('Enter name:'))
                                        c.send(fname)
                                        sname = str(input('Enter surname name:'))
                                        c.send(sname)
                                        address = str(input('Enter address:'))
                                        c.send(address)

                                        result = c.recv()
                                        print(result)
                                        continue
                                else:
                                        #If phone exists this will be printed
                                        print('Phone exists, customer with phone %s is already registered' % phone)
                                        continue
                                
                        elif Cho == '2':
                                print('Register Item')
                                print()
                                #videoVer = str(input('Enter Movie version:'))
                                #c.send(videoVer)
                                vname = str(input('Enter movie name:'))
                                c.send(vname)
                                vtype = str(input('Enter type:'))
                                vtype.upper()
                                if vtype == 'R':
                                        c.send(vtype)
                                elif vtype == 'B':
                                        c.send(vtype)
                                else:
                                        print("Error: Movie type can ONLY be 'R' - for new or 'B' - for old Movies")
                                        
                                c.send(vtype)
                                
                                result = c.recv()
                                print(result)
                                continue
                        
                        elif Cho == '3':
                                print('Hire Out Movie')
                                print()
                                phone = str(input('Please enter the phone you registered with:'))
                                c.send(phone)
                                videoId = str(input('Please enter the Id of the movie you would like to hire:'))
                                c.send(videoId)
                                
                                result = c.recv()
                                print(result)
                                continue
                        elif Cho == '4':
                                print('Return Movie')
                                print()
                                videoId = str(input('Please enter the Id of the movie you hired:'))
                                c.send(videoId)

                                result = c.recv()
                                print(result)
                                continue
                        
                except ValueError:
                        print ('Enter a valid value')
                        #print('server reply:', server_reply)
                        continue
                else:
                        print('Error:')
                        continue
