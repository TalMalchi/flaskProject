# Final Attendence Project - DevOps Bootcamp



This project represents an application made with Falsk (Python) that connects to DataBase (MySql).  
The application shows the attendence of each student in the course.
My application will build with ****docker-compose****.The Database, and the backend of the app will be in different containers, and `docker-compose.yaml` file will connect between them.

### :1st_place_medal: Using: 

<span>
  <img src="https://skillicons.dev/icons?i=python,flask,mysql,github,git,linux,docker,jenkins,aws" />
</span>

### :bowing_woman: About
Given csv files that Webex takes out after every session, we have to calcuate the the percentage of attendance of each student.
This function has done by **_yona bloy_** https://github.com/natibloy/bynet.git .  
I will connect to Sql server, insert to a table the final csv file we get from attendence function.  
My app will connect to the same sql server- using the same database and the same port, get all the data and share to web application.


### :bookmark_tabs: Explanation about the classes   
- ***db***  - Init the DataBase using MySql. Create new data base, and new table, that will be used by our application.  
- ***BackEnd*** - Init the application using Flask. Connects to the database, read all the data, post it to the app, and shares it to the browser.   
- ***templates*** - Represent all the FrontEnd of the app.  


### :infinity: CI/CD  
I will use 3 seperate aws machine- for Jenkins, for testing, and for production.
All of the machines will be connect with ssh, and private and public keys.  
I will create a pipeline using Jenkins, that will build, test and deploy the code automaticly.    
The purpose of this proccess is to minimize human error and maintain a consistent process for how software is released.   
Each time there is any change in the code, i will commit it to GitHub. Jenkins will be triggerd by poll SCM (every few minute), and Jenkins machine will pull the changes from the repository.    
The first machine will check the changes, and will build a new image- using the docker file (in the BackEnd directory).  
The new image will be push to DockerHub. 
Then Jenkins machine will transfer the project to test machine, using scp, that will test the app.   
After all the tests pass, it will pass to production machine to desploy the app.  
Both Test and Production machine will use the ***desploy.sh*** script.
         

<img width="800" alt="Screenshot 2022-11-04 152518" src="https://user-images.githubusercontent.com/93086649/199983523-302ebecd-e0e7-494f-89fc-3b14c3cc1663.png">

![Screenshot 2022-11-04 153750](https://user-images.githubusercontent.com/93086649/200024503-c5e20fbe-6b6c-4efd-85b8-7f49f69d28b4.png)



### :sparkles: System Desgin   

<!--<img width="700" alt="198629176-ede46079-dd6f-426d-8ff7-54c8960decf2" src="https://user-images.githubusercontent.com/93086649/198629554-efb7969c-3dbd-4ff3-aa89-851131717555.png">-->
<img width="800" alt="project diagram" src="https://user-images.githubusercontent.com/93086649/200297592-32963099-f2e8-4a4a-a428-0627d488e90c.png">





### :running_woman: How to run?
```python
- Clone the project 
- Make sure you have Docker && docker-compose installed on your computer
- Run on your terminal `docker-compose build` Then `docker-compose up`
- Open your browser on `localhost:5005`
```

### :movie_camera: Video of the Project 



https://user-images.githubusercontent.com/93086649/200306409-ad9c6f43-0e11-4988-8468-d1662ad1b0cd.mp4




<!--https://user-images.githubusercontent.com/93086649/194543363-ce1c2b23-faec-4ee5-b2a9-10d23b1b21e8.mp4 -->





