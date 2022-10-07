## Attendence Project

This project represent an application made with Falsk (on Python) that connects to DataBase (using MySql).
The application shows the attendence of each student in the course

### How it works?
Given csv files that Webex takes out after every session, we have to calcuate the The percentage of attendance of each student.
This file has done by **_yona bloy_** https://github.com/natibloy/bynet.git .  
We will connect to Sql server, insert to a table the final csv file we get from attendence function.  
Our app will connect to the same sql server- using the same database and the same port, get all the data and share to web application.
**docker-compose** will connect between the DataBase and the application.

***BackEnd Directory*** - Init the application using Flask. Read all the data from the DataBase and share it to the app.  
***db Directory***  - Init the DataBase. Create new data base using MySql, and new table for the app.


#### How to run?
- Clone the project 
- Make sure you have Docker installed on your computer
- Run on your terminal `docker-compose up`
- Open your browser on `localhost:5005`




https://user-images.githubusercontent.com/93086649/194543363-ce1c2b23-faec-4ee5-b2a9-10d23b1b21e8.mp4




