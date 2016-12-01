**Data Representation and Querying Project 2016**
===
This repository contains all the files and code for my third-year undergraduate project for the module Data Representation and Querying.
Project Idea
---
My plan for my project was to devise a single web page application where the user can store all information about different types of drinks and they can have a database knowing how many calories are in certain drinks.

My plan for the opening page of the app is to allow the user to log in to an account. They will be able to log in with the right credentials. Once logged in, they will be able to store information about a certain drink and how many calories are in that drink. I also planned to have some basic facts about some drinks inside the web application, but this caused the web application to look untidy & cluttered so I decided to leave these facts out.

How my Project Works
---
When my project runs, it will bring you to a log in page. The user must enter the correct credentials, which in my project is set to **(Username = admin)** and **(Password = admin)**. The user will not be able to access any other part of the web application unless the user is logged in.

I achieved this by using sessions. Sessions allowed me to restrict access to pages I didn’t want just anybody to enter. Sessions will only allow the user who has logged in with the correct credentials access pages beyond the log in page.

Once logged in, the user will be asked to input basic information about any drink. They will be able to input information about the name of the drink and the number of calories in that drink. The information will be stored underneath the inputs.

Problems
---
I encountered a problem with my project when I started trying to insert a database. I wanted to allow the user to input the name of a drink and the calories in the drink to a table in the HTML file softDrinks. I tried mongoDB, couchDB and SQlite3 but was unsuccessful with all three of them. I ended up leaving SQlite3 in my project as I could allow the user to input one piece of data so I could demonstrate how I wanted my web application to turn out. I will hopefully in the future figure out how it is possible to use a database properly with Python and Flask.

How to run my web application
---
My application uses Python 3 and Flask. Both must be installed to run the web application.

If you need to install these onto your system, here are 2 good links that will help you in your setup.

Python - http://www.howtogeek.com/197947/how-to-install-python-on-windows/

Flask - http://flask.pocoo.org/docs/0.10/installation/

I also use SQLite3 in my application but since I have a db.sql directory inside of my repository there is no need to install anything else for SQLite to run.

Once you have these requirements installed you will be able to run the web application. To do so you must use the command prompt and commute to the folder of the web application and run the following:

```bash
* python startPage.py
```

Once the application is running, you can access it by copying the URL giving to you which should be http://127.0.0.1:5000/, and pointing it to your browser.

Architecture
---
This web application runs in Python 3 using the Flask web micro-framework and uses SQLite as a database. I chose to use SQLite as it was easiest to use and I could find a lot of information on the internet on how to use SQLite. I was unsuccessful in getting SQLite3 to work correctly with my web application, but I did find it more straight forward compared to other databases.

References
---
The following are references to samples of code that I researched and used in my project. I have commented all reference links in my code also.

For the login.HTML file - http://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_temp_webpage&stacked=h – I used this as a template for the look of this page.

For the softDrinks.HTML file I used the same link as a template for the page. I also used a template for the table in the page - https://www.sanwebe.com/2014/08/css-html-forms-designs .

In the startPage.py file I used code I researched for the login code decorator - https://pythonprogramming.net/decorator-wrappers-flask-tutorial-login-required/ .

