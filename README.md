# [Jeffblog](https://blogjeff.herokuapp.com/)
## Jeffblog is a web application for adding up blogs and commenting on existing blogs.
### Sept,14,2018
#### By **[Jeff Musa](https://github.com/jeffmusa)**

## Description
Jeffblog is a web application blog meant inspirational blogs and all that comes along with positivity.

The blog supports comments from readers and blog writers to determine whether to delete the comments or not. Users can also delete blog posts.

After the writer has posted a new blog post, subscribers will receive an email notification with a link to the blog post.


## Set-up and Installation

### Prerequiites
    - Python 3.6
    - Ubuntu software

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/jeffmusa/Blog-IP.git && cd Blog-IP`

Install [Postgres](https://www.postgresql.org/download/)
### Create a Virtual Environment
Run the following commands in the same terminal:
```bash
sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements`

### Prepare environment variables
```bash
export DATABASE_URL='postgresql+psycopg2://<your-username>:<your-password>@localhost/carblog'
export SECRET_KEY='Your secret key'
export DATABASE_URL_TEST='postgresql+psycopg2://<your-username>:<your-password>@localhost/carblog_test'
export MAIL_SERVER='smtp.googlemail.com'
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME=<your-email>
export MAIL_PASSWORD=<your-password> 
```

### Run Database Migrations
```bash
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```
### Running the app in development
In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

## Known bugs
Sending batch emails bug


## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details
Contact me on jeffmusa05@gmail.com for advice.

### License
Copyright (c) **Jeff Musa**
