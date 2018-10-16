# awwardIT
This is a python app made with Django.
This web app is an awarding site where users submit their projects and other users get to  review and rate them. 
 
<img src="http://cleardarksky.com/csk/getcsk.php?id=AftnCyCCA">
    
## Purpose
The purpose of this Independent Project is to demonstrate your level of understanding of the various concepts in python django .
Its also a chance to make further exploration and implement extra functionality.

# Additional Information
    Before you start building the project, make sure you have python installed in your device.

# References
    If you get stuck during the development of your project try checking your code well.
    Identation matters alot.


# Project prompt
    At Moringa school many projects have been done (IPs, Mid-week projects) but no rating by users is done. Your objective is to create an application like Awwards. (It doesn't necessarily have to be exactly the same). The application will allow a user to post a project he/she has created and get it reviewed by those who use it.

A project can be rated based on 3 different criteria

    Design
    Usability
    Content
    These criteria can be reviewed on a scale of 1-10 and the average score is taken.

# User stories
As a user, you can:

    View posted projects and their details.
    Post a project to be rated/reviewed
    Rate/ review other users' projects
    Search for projects 
    View projects overall score
    View my profile page.

## System Features/Objectives
     Projects
Projects should have a Title, an image of the project's landing page, a detailed description of the project, a link to the live site.

     Profile
Your project should have a user profile that at least the following information:

    Profile picture of the user.
    User Bio
    Projects the user has posted
    A contact information of the user. 
 An Authentication System 
    Your application should have a solid authentication system that allows users to sign up or log in to the application before posting or rating a project.

    
 
##  API Endpoints
    You should create an API so that users can access data from your application. You can create two API endpoints:

Profile - This endpoint should return all the user profiles with information such as the username, bio, projects of the user and profile picture
Projects- This endpoint should return information pertaining to all the projects posted in your application.


## API Endpoints (url / uri)
    - CRUD : Create, Retrieve, Update, Delete 
    - Create List and Search

## HTTP methods (client side)
    - GET, POST, PUT, MATCH, DELETE    
    
## Data Types and Validation
    Use a serializer for consistency 
    JSON -> Serializer
    Validation -> Serializer

# Getting Started.

    These instructions will get you a copy of the project running on a local host.

    Step 1: git clone - https://github.com/Jeffmusa/awwardIT.git
    Step 2: Enter the Project root folder

    cd awwardIT/
    install virtual environment (venv) without pip

    python3.6 -m venv --without-pip virtual
    Step 3: Activate virtual environment

    source virtual/bin/activate
    install pip using curl


## Deployment

    This project should be  deployed to heroku.
    Deploying is a process and here is hhow to do it.

[Deploy to heroku](https://github.com/Jeffmusa/Deployment_to_heroku_django).

## Built With

* [Python3.6.5](https://docs.python.org/3/) - Python is a programming language that lets you work quickly and integrate systems more effectively
* [Django framework](https://docs.djangoproject.com/en/2.1/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design
* [Postgresql](https://www.postgresql.org/docs/) - PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.
    Versioning
    version 1.0.0
 [Heroku](https://dashboard.heroku.com) -For hosting the app

## Bugs

    No known bugs but any found can be reported
    jeffmusa05@gmail.com
## Author

Jeff Musa

## License

This project is licensed under the MIT License

## Acknowledgments

Moringa School


