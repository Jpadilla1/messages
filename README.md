Messages
========

Small example Django &amp; nodejs app using webhooks and websockets.

##Installation

###Python

For this project you will need python 2.7.x installed on your computer.
You can download the python installer [here.](https://www.python.org/downloads/)

**Note: Depending on your Operating system, you may have python already installed.**

To check if you have python installed, you can try the following in the command line.

```bash
$ python
```

This will get you to the python shell and it also provides the python version that's installed.

###Virtual Environment

This is not necessary, but it is highly recommended. A virtual environment is a place where
you can work separately from your global environment and install everything you want and never
affect your global environment.

To do this in python, you can install `virtualenv` with `easy_install` or `pip`. We recommend `pip`.

```bash
$ sudo pip install virtualenv
```

To create a `virtualenv`, select a folder where you want to work with the project and do the following:
 
```bash
$ virtualenv venv
```

That will create a virtual environment for python. To activate it do the following:

```bash
$ source venv/bin/activate
```

###Dependencies

Now that you are in your venv, let's take care of project dependencies.

In the command line, go to the projects root folder and do the following:

```bash
$ pip install -r requirements.txt
```

That will install all of the dependencies of the Django app.

Now you need to install the nodejs dependencies. Go to the node_app directory and run this:

```bash
$ npm install
```

That will install the necessary node modules for this project.

###Database

To create the database do the following:

```bash
$ python manage.py syncdb
```

It will ask to create a superuser account. Please do so.

###Running the project

Now, you can run the Django app from the root directory.

```bash
$ python manage.py runserver
```

To run the node server just run this in the node_app directory:

```bash
$ node app.js
```

###Usage

Open up [http://localhost:8000/api/messages](http://localhost:8000/api/messages) in your browser. This is the Django server.

Now, in a new browser tab, go to [http://localhost:3000/](http://localhost:3000/). You will see blank screen. This is the nodejs server.

For a better view angle, separate the tabs into 2 separate windows and go to the Django app window and scrool to the bottom.
You should see a small form. Now enter any message and select your account and click POST. You should see the message pop out the nodejs server screen.

Now this is something we are use to see in just a plain nodejs app with socket.io right? So why complicate it with Django?
Well, I wanted to try out webhooks for the first time but I wanted to see the results in realtime in the UI. So, when the message is sent, it does the following:

- Stores the message in the database.
- Does a `POST` to the WEBHOOK_URL with the message data.
- The Node app receives it and emits the message off to the websocket.
- The message gets displayed on the screen.

That's pretty a summary of what this app does. It was really fun doing it and get a feel of how realtime apps work.

Have fun using it! :)
