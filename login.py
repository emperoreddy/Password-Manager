# TODO create login system
# TODO create a way to change the password of user

import database as db


class User():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.id = db.id_credentials_index
        db.create_table_credentials()
        

    def register_user(self):
        db.create_user_credentials(self.username, self.password)
        db.create_database(self.username)

    def login_user(self):
        db.get_user_credentials(self.username, self.password)

        

   
def create_user(username, password):
    user = User(username, password)
    return user
    


'''
LOGIN: check if the user exists
if yes, check if the password is correct
if yes, go to the user's table

CREATE A NEW PASSWORD: go to the credentials table and change the user's password 
'''
