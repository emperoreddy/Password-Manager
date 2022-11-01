import database as db


def get_credentials():
    app = input('App name: ')
    username = input('Username: ')
    return app, username


def user_choice():
    db.create_user()
    print("\nWhat would you like to do? (1-5) ")
    print('----------------------------------------------------------')
    print('''
    1. Create a new password
    2. Delete a password
    3. Get a password
    4. Get all passwords
    5. Delete all passwords (WARNING: This will delete all your passwords)
    ''')
    print('----------------------------------------------------------')
    

    choice = input()

    if choice == '1':
        credentials = get_credentials()
        password = input('Password: ')
        # app, username, password
        db.insert_user(credentials[0], credentials[1], password)

    elif choice == '2':
        credentials = get_credentials()
        db.delete_user(credentials[0], credentials[1])  # app, username

    elif choice == '3':
        credentials = get_credentials()
        db.get_password(credentials[0], credentials[1])  # app. username

    elif choice == '4':
        db.get_all_passwords()

    elif choice == '5':
        db.delete_all()

    repeat = input('\nWould you like to do anything else? (y/n) ')
    if repeat == 'y' or repeat == 'Y':
        user_choice()
    else:
        print('Thank you for using this program')
        exit()


if __name__ == "__main__":
    # db.create_user('sql.db')
    # db.get_user()
    user_choice()
