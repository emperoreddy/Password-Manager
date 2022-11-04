import sqlite3


DATABASE = r"D:\PROGRAMARE\PYTHON\Learning\Backend\database\sql.db"
id_credentials_index = 1

# CONNECTION 
global user
try:
    user = sqlite3.connect(DATABASE)
except sqlite3.Error as e:
    print(e)




def database_is_empty(result):
    return result.__len__() == 0


def credentials_username_is_valid(username):
    elements = user.execute(
        f"SELECT username FROM credentials WHERE username='{username}'")
    result = elements.fetchall()

    return not database_is_empty(result)


def login_credentials_are_valid(username, password):
    elements = user.execute(f'''
    SELECT username, password FROM credentials WHERE username='{username}' AND password='{password}'
    ''')
    result = elements.fetchall()
    return not database_is_empty(result)


# CREATE
def create_database(login_username, database=DATABASE):
    user.execute(
        f'CREATE TABLE IF NOT EXISTS {login_username}_passwords (app VARCHAR(50) PRIMARY KEY, username VARCHAR(50), password VARCHAR(50))')
    print(f"Database {login_username}_passwords created successfully")
    user.commit()


def create_table_credentials():
    user.execute(
        '''
    CREATE TABLE IF NOT EXISTS credentials
(
    user_id  INTEGER primary key autoincrement ,
    username VARCHAR(50),
    password VARCHAR(50)
)
    ''')


def create_user_credentials(username, password):
    while credentials_username_is_valid(username):
        username = input("Username already exists, choose another one: ")
    else:
        user.execute(
            f"INSERT INTO credentials (username, password) VALUES ('{username}', '{password}')")
        user.commit()


# def create_user_password_table(username):
#     user.execute(f'''
#     CREATE TABLE IF NOT EXISTS {login_username}_passwords
#     ''')


# INSERT
def insert_password(app, username, password, login_username):
    user.execute(
        f"INSERT INTO {login_username}_passwords VALUES ('{app}', '{username}', '{password}')")
    user.commit()


# SELECT
def get_all_passwords(login_username):
    #Gets all the elements in the database

    elements = user.execute(f'SELECT * FROM {login_username}_passwords')
    result = elements.fetchall()

    # check if the database is empty
    if database_is_empty(result):
        print('No passwords found')
    else:
        for row in result:
            print(f'App: {row[0]} \tUsername: {row[1]} \t\tPassword: {row[2]}')

    print('----------------------------------------------------------')


def get_password(app, username, login_username):
    '''
    Gets the password of the app
    :param app: The name of the app
    '''
    elements = user.execute(
        f"SELECT password FROM {login_username}_passwords WHERE app='{app}' AND username='{username}'")
    result = elements.fetchall()

    # check if the database is empty
    if database_is_empty(result):
        print('No password found, try to create one')
    else:
        for row in result:
            print(f'\nUsername: {username}\nPassword: {row[0]}')
    print('----------------------------------------------------------')


def get_user_credentials(username, password):
    while login_credentials_are_valid(username, password):
        print("Login successful")
    else:
        print("Wrong credentials, try again")



# DELETE
def delete_username_password(app, username, login_username):
    # Deletes a row from the database

    user.execute(
        f"DELETE FROM {login_username}_passwords WHERE app='{app}' AND username='{username}'")
    user.commit()


def delete_all_users_passwords(login_username): # deletes passowrds from the user's table (only the logged one)
    user.execute(f"DELETE FROM {login_username}_passwords")
    user.commit()


def delete_all_users_credentials():
    user.execute("DELETE FROM credentials")
    user.commit()


# CLOSE CONNECTION
def close_connection():
    if user:
        user.close()
        print("Connection closed")
