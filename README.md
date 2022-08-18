# inforce-test-task
## A service that will make your life easier. You can vote for menu in just a few clicks!




## Installing from GitHub



```sh
git clone https://github.com/BohdanKryven/inforce-test-task.git
cd inforce-test-task
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
set DB_HOST=<db_hostname>
set DB_NAME=<db_name>
set DB_USER=<db_username>
set DB_PASSWORD=<db_password>
set SECRET_KEY=<your secret key>
python manage.py runserver
```

## Also, you can run using Docker

```sh
sudo docker-compose build
sudo docker-compose up
```

## Getting access
- create user on /api/user/register/
- get access token on /api/user/token/
- verify token on  api/token/verify/



## Features

- Authentication with JWT Token
- Managing Restaurant, Votes
- Powerful admin panel for advanced managing

