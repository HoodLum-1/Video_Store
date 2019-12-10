# Video_Store 📹 🎥
  Python Client Server, Video Store 
  Back-end python system for a video store with sql database.

# Description 📜
  System that will enable a video store to keep record of all their
  customers as well as their videos. The system has a server and client side. The server connects to a
  MySQL database called “video_store”. When the client request certain data from the server, the
  server will have to process the request and send back the result to the client.

  Each customer must be registered on the system to be able to hire out movies. The customers’
  details are all stored in the database table called “customers”

## Run/Install ⏳💻

  Ensure you have MySQL and MySQL_python connector installed. 🔧 
  Change the connection settings in "video store.py" to align with those of you installation.🔌
  
  ```python
try:
	conn = mysql.connector.connect(
	user='root',
	password='MySQL',
	host='localhost'
	)
```
  
  Run the pyton scripts in the following order
  "video store.py"
  "Server.py"
  "Client.py"
  And follow the screen prompts.💻

## Customer registration: 📝 📝
  When the register option is chosen, the customer must enter their phone number, the server will
  then check if the customer is not already registered. If the customer already exists a message will be
  printed to indicate this, else the user can continue with their registration and enter their details as
  follows: Name, Surname and address, which will be sent to the server and upon the print of
  “customer successfully registered message the new customer is registered.

## Movies registration: 🎬
  When the register movie option is selected, the user must enter the movie name and type which can
  only be of the following types “Red box indicated by, ‘R’ for new movies” or “Black box indicated by
  ‘B’ for old movies, the information is then sent to the server and the movies is add to the database in
  the videos table.

## Hire Out movie:📺 🎥
  When the hire out movie option is selected the application will ask for the customers phone number
  and the Id of the movie they would like to hire, the customer details are retrieved if they match the
  phone number inputted, The movies is marked as hired out by it being added to the hire table
  indicated the date hired as well.

## Return Movie:◀️ ⏪
  This option requests the id of the movie hired and it is marked as returned by updated the hire table
  on the returned date column.

## Screen shots:📷
  Coming soon...
