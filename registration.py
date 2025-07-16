import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="aptech"
)
cursor = con.cursor()


def sign_up():
    print("\n------ SIGN UP: CREATE A NEW ACCOUNT ------")
    name = input("Enter your full name: ")
    username = input("Choose a username (max 18 chars): ")
    password = input("Choose a password (max 18 chars): ")

    if username == password:
        print("Username and password cannot be the same!")
        return
 
    cursor.execute("SELECT * FROM user_auth WHERE username = %s", (username,))
    if cursor.fetchone():
        print("That username already exists. Choose another.")
        return


    cursor.execute("INSERT INTO user_auth (name, username, password) VALUES (%s, %s, %s)", (name, username, password))
    con.commit()
    print(" Account created successfully!")


def log_in():
    print("\n------ LOG IN TO YOUR ACCOUNT ------")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    cursor.execute("SELECT * FROM user_auth WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    if user:
        print(f"\n Login successful! Welcome back, {user[1]} ")
    else:
        print(" Invalid username or password. Please try again.")


def main():
    while True:
        print("\n========== USER AUTHENTICATION SYSTEM ==========")
        print("1. Log In")
        print("2. Sign Up")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            log_in()
        elif choice == "2":
            sign_up()
        elif choice == "3":
            print(" Exiting... Bye Queen!")
            break
        else:
            print(" Invalid input. Please enter 1, 2, or 3.")

    cursor.close()
    con.close()
main()
