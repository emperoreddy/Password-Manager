import database as db
import login


def choice_message_before_login():
    print('''
    ----------------------------------------------------------
    1. Login
    2. Register
    3. Exit
    ----------------------------------------------------------
    ''')


def choice_message_after_login():
    print("\nWhat would you like to do? (1-5) ")
    print('''
    ----------------------------------------------------------
    1. Create a new password
    2. Delete a password
    3. Get a password
    4. Get all passwords
    5. Delete all passwords (WARNING: This will delete all your passwords)
    6. Logout
    7. Exit
    ----------------------------------------------------------
    ''')


def get_credentials():
    app = input('App name: ')
    username = input('Username: ')
    return app, username


def user_choice_before_login():
    choice_message_before_login()
    choice = input()
    global login_username
    if choice == '1':
        login_username = input('Username: \n')
        login_password = input('Password: ')
        user = login.create_user(login_username, login_password)
        if db.login_credentials_are_valid(login_username, login_password):
            user_choice_after_login()
        else:
            print('Wrong credentials, try again')
            user_choice_before_login()
        
    elif choice == '2':
        login_username = input('Username: \n')
        login_password = input('Password: ')
    
        user = login.create_user(login_username, login_password)
        user.register_user()

    elif choice == '3':
        print('Thank you for using this program')
        exit()



def user_choice_after_login():
    choice_message_after_login()
    choice = input()

    if choice == '1':
        credentials = get_credentials()
        password = input('Password: ')
        db.insert_password(credentials[0], credentials[1], password, login_username) # app, username, password

    elif choice == '2':
        credentials = get_credentials()
        db.delete_username_password(
            credentials[0], credentials[1], login_username)  # app, username

    elif choice == '3':
        credentials = get_credentials()
        db.get_password(credentials[0], credentials[1], login_username)  # app. username

    elif choice == '4':
        db.get_all_passwords(login_username)

    elif choice == '5':
        db.delete_all_users_passwords(login_username)
    
    elif choice == '6':
        user_choice_before_login()
    
    elif choice == '7':
        print('Thank you for using this program')
        exit()

    repeat = input('\nWould you like to do anything else? (y/n) ')
    if repeat == 'y' or repeat == 'Y':
        user_choice_after_login()
    else:
        print('Thank you for using this program')
        exit()


if __name__ == "__main__":
    
    user_choice_before_login()
    user_choice_after_login()
