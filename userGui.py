import database as db
import login


def choice_message_before_login():
    print('''
    ----------------------------------------------------------
    1. Login
    2. Register
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
    ----------------------------------------------------------
    ''')


def get_credentials():
    app = input('App name: ')
    username = input('Username: ')
    return app, username


def user_choice_before_login():
    choice_message_before_login()
    choice = input()
    if choice == '1':
        # login.login()
        pass
    elif choice == '2':
        username = input('Username: \n')
        password = input('Password: ')
        user = login.create_user(username, password)
        user.register_user()


def user_choice_after_login():
    db.create_database()
    choice_message_after_login()
    choice = input()

    if choice == '1':
        credentials = get_credentials()
        password = input('Password: ')
        # app, username, password
        db.insert_password(credentials[0], credentials[1], password)

    elif choice == '2':
        credentials = get_credentials()
        db.delete_username_password(
            credentials[0], credentials[1])  # app, username

    elif choice == '3':
        credentials = get_credentials()
        db.get_password(credentials[0], credentials[1])  # app. username

    elif choice == '4':
        db.get_all_passwords()

    elif choice == '5':
        db.delete_all_users_passwords()

    repeat = input('\nWould you like to do anything else? (y/n) ')
    if repeat == 'y' or repeat == 'Y':
        user_choice_after_login()
    else:
        print('Thank you for using this program')
        exit()


if __name__ == "__main__":
    db.create_database()
    user_choice_before_login()
