import sqlite3


DATABASE = r"D:\PROGRAMARE\PYTHON\Learning\Backend\database\sql.db"
id_credentials_index = 1


def database_is_empty(result):
    return result.__len__() == 0


def credentials_username_is_valid(username):
    elements = user.execute(
        f"SELECT username FROM credentials WHERE username='{username}'")
    result = elements.fetchall()

    return not database_is_empty(result)

# CREATE


def create_database(database=DATABASE):
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


def insert_user_credentials(username, password):
    while credentials_username_is_valid(username):
        username = input("Username already exists, choose another one: ")
    else:
        user.execute(
            f"INSERT INTO credentials (username, password) VALUES ('{username}', '{password}')")
        user.commit()


# INSERT
def insert_password(app, username, password):
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
def get_all_passwords():
    '''
    Gets all the elements in the database
    '''
    elements = user.execute('SELECT * FROM test')
    result = elements.fetchall()

    # check if the database is empty
    if database_is_empty(result):
        print('No passwords found')
    else:
        for row in result:
            print(f'App: {row[0]} \tUsername: {row[1]} \t\tPassword: {row[2]}')

    print('----------------------------------------------------------')


def get_password(app, username):
    '''
    Gets the password of the app
    :param app: The name of the app
    '''
    elements = user.execute(
        f"SELECT password FROM test WHERE app='{app}' AND username='{username}'")
    result = elements.fetchall()

    # check if the database is empty
    if database_is_empty(result):
        print('No password found, try to create one')
    else:
        for row in result:
            print(f'\nUsername: {username}\nPassword: {row[0]}')
    print('----------------------------------------------------------')


# DELETE
def delete_username_password(app, username):
    '''
    Deletes a row from the database
    :param app: The name of the app
    :param username: The username of the app
    '''
    user.execute(
        f"DELETE FROM test WHERE app='{app}' AND username='{username}'")
    user.commit()


def delete_all_users_passwords():
    user.execute("DELETE FROM test")
    user.commit()

def delete_all_users_credentials():
    user.execute("DELETE FROM credentials")
    user.commit()



# CLOSE CONNECTION
def close_connection():
    if user:
        user.close()
        print("Connection closed")
