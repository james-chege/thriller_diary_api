# thriller_diary_api

# status
[![Build Status](https://travis-ci.org/james-chege/thriller_diary_api.svg?branch=develop)](https://travis-ci.org/james-chege/thriller_diary_api)
[![Coverage Status](https://coveralls.io/repos/github/james-chege/thriller_diary_api/badge.svg?branch=develop)](https://coveralls.io/github/james-chege/thriller_diary_api?branch=develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/94c03ff0c47e423eb0c993cfa4c7f458)](https://www.codacy.com/app/james-chege/thriller_diary_api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=james-chege/thriller_diary_api&amp;utm_campaign=Badge_Grade)

[__Live version__](http://api-thriller-diary.herokuapp.com/api/v1/auth)

[Api Documentation](http://api-thriller-diary.herokuapp.com/apidocs/)


### Local Installation

Fork this repository to your github account and clone from there(_NB: clone from your github account - after forking_).This will help you to contribute to this project.

[Create a python Virtual environment and Activate it](https://virtualenv.pypa.io/en/stable/). A virtual environment is effective when working on multiple projects. Each project will have its own development enviroment.

__Install Dependencies__(_Note: This should be done in the created virtual environment_)
```py
 pip install -r requirements.txt
```
__Set environment variable__
```py
 export APP_SETTINGS="development"
```

# setup Database
* make sure you have [__postgresql__](https://www.postgresql.org/download/linux/ubuntu/) installed and running properly.

* Change the connection details in `db.py` and `create_db.py` to match yours.

On the root folder of this project run __`python create_db.py`__ to create database for the Api.


* __Creating database for testing__
To create database for testing, run __`python create_test_db.py`__.


__Start Server__
```py
python run.py
```

[__Use postman app to send request to app.__](https://www.getpostman.com/)
### Endpoints

The following is a list of available endpoints in this application

|EndPoint               | Functionality|
| ------------------------------------ | ------------------------ |
|POST api/v1/auth/signup    |Register a user|
|POST api/v1/auth/login |Login a user|
|GET api/v1/entries |fetch all entries|
|GET api/v1/entries/<int:entryId> |fetch a single entry|
|POST api/v1/entries |Add an entry|
|PUT api/v1/entries/<int:entryId> |modify an entry|

# Testing
py.test --cov=app
