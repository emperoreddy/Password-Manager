import sqlite3


DATABASE = "./database/sql.db"

# CREATE
def create_user(database=DATABASE):
    '''
    Creates a new database
    :param database: The name of the database
    :return: None
    '''
    global user
    try:
        user = sqlite3.connect(database)
    except sqlite3.Error as e:
        print(e)
    else:
        user.execute(
            'CREATE TABLE IF NOT EXISTS test (app VARCHAR(50) PRIMARY KEY, username VARCHAR(50), password VARCHAR(50))')
        print("Database created successfully")
        user.commit()


# INSERT
def insert_user(app, username, password):
    '''
    Inserts a new row of data into the database
    :param app: The name of the app
    :param username: The username of the app
    :param password: The password of the app
    :return: None
    '''
    user.execute(
        f"INSERT INTO test VALUES ('{app}', '{username}', '{password}')")
    user.commit()


# SELECT
def get_user():
    '''
    Gets all the elements in the database
    '''
    elements = user.execute('SELECT * FROM test')
    for row in elements:
        print(row)


def get_password(app, username):
    '''
    Gets the password of the app
    :param app: The name of the app
    '''
    password = user.execute(f"SELECT password FROM test WHERE app='{app}' AND username='{username}'")
    for row in password:
        print(f'\nUsername: {username}\nPassword: {row[0]}')


# DELETE
def delete_user(app, username):
    user.execute(f"DELETE FROM test WHERE app='{app}' AND username='{username}'")
    user.commit()


def delete_all():
    user.execute("DELETE FROM test")
    user.commit()


# CLOSE CONNECTION
def close_connection():
    if user:
        user.close()
        print("Connection closed")


