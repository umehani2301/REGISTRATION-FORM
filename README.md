# User Authentication System with Python & MySQL

This is a basic sign-up and login system built using Python and MySQL Connector.  
It allows users to create an account and log in securely using a MySQL database.

## 🚀 Features

- User registration (Sign Up)
- Login validation
- Password hidden during input using `getpass`
- MySQL backend connection

## 🛠️ Technologies Used

- Python
- MySQL
- `mysql-connector-python` package

## 🧾 Table Structure

```sql
CREATE TABLE user_auth (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50)
);
