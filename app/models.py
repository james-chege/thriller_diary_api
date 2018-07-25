"""
app/models.py
contains models for the app
"""
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
import psycopg2
import datetime
from flask_jwt import jwt
import os 
from functools import wraps
from flask import request, jsonify, current_app, session

class Entry(object):
    """Add new entry"""
    # constructor
    def __init__(self):
        # all entries placeholder
        self.entries = []
        HOSTNAME = 'localhost'
        USERNAME = 'postgres'
        PASSWORD = '2grateful'
        DATABASE = 'thriller'
        self.db = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

    def add_entry(self, title, description, current_user):
        """Adds new entries"""

        if description and title:
            now = datetime.datetime.now()
            date_created = now.strftime("%Y-%m-%d %H:%M")

            # entry id
            entry_id = 1
            for i in self.entries:
                entry_id += 1
                if i['id'] == entry_id:
                    entry_id += 1
            # single_entry_holder = dict()
            # single_entry_holder['id'] = entry_id
            # single_entry_holder['title'] = title
            # single_entry_holder['description'] = description
            # single_entry_holder['created'] = str(date_created)
            # self.entries.append(single_entry_holder)
            owner_id = current_user
            cur = self.db.cursor()
            query =  "INSERT INTO entries (title, date_created, description, owner_id) VALUES (%s, %s, %s, %s)"
            data = (title, date_created, description, owner_id)
            cur.execute(query, data)
            self.db.commit()

            # return true
            return 1

        # on failure to add return false
        return 0


    def all_entries(self):
        """Return available entries"""

        return self.entries

class User:
    """ returns available users """
    def all_the_users(self):
        """Returns all users in databse """
        HOSTNAME = 'localhost'
        USERNAME = 'postgres'
        PASSWORD = '2grateful'
        DATABASE = 'thriller'
        db = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cur = db.cursor()
        cur.execute("SELECT id, username, email, password FROM users")
        return cur.fetchall()

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None

        if 'access-token' in request.headers:
            token = request.headers['access-token']

        if not token:
            return jsonify({'message' : 'Please provide a token', 'token' : request.headers}), 401

        try:
            data = jwt.decode(token, 'shark')
            current_user = data['user_id']
        except:
            return jsonify({'message' : 'Provided token is invalid, try again'}), 401

        return func(current_user, *args, **kwargs)

    return decorated
    