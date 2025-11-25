import loginLib

def show_main_menu():
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")


def show_user_menu():
    print("User menu:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")


def user_session(username: str):
    while True:
        show_user_menu()
        choice = input("Your choice: ")

        if choice == "1":
            profile = loginLib.viewProfile(username)
            if profile:
                print(f"Profile ID {profile[0]} - {profile[1]}")
                print()
        elif choice == "2":
            newp = input("Insert new password: ")
            loginLib.change_password(username, newp)
            print("Password changed.")
            print()
        elif choice == "0":
            print("Logging out...")
            print()
            return
        else:
            print("Invalid choice.")
            print()


def handle_login():
    username = input("Insert username: ")
    password = input("Insert password: ")

    if loginLib.login(username, password):
        print("Authentication successful!")
        print()
        user_session(username)
    else:
        print("Invalid credentials.")
        print()


def handle_register():
    username = input("Insert username: ")
    password = input("Insert password: ")

    if loginLib.viewProfile(username):
        print("Username already exists.")
        print()
        return

    loginLib.register(username, password)
    print("User registration completed.")
    print()


def main():
    print("Program starting.")
    while True:
        show_main_menu()
        choice = input("Your choice: ")

        if choice == "1":
            handle_login()
        elif choice == "2":
            handle_register()
        elif choice == "0":
            print("Exiting program.")
            print()
            break
        else:
            print("Invalid choice.")
            print()

    print("Program ending.")


if __name__ == "__main__":
    main()
