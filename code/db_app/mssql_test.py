import os
import pyodbc

def create_connection():
    """ Create a database connection to the MSSQL database. """
    db_host = os.getenv('MSSQL_HOST')
    db_user = 'sa'  # Using the SA user
    db_password = os.getenv('SA_PASSWORD')
    db_database = os.getenv('MSSQL_DB')

    conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={db_host};DATABASE={db_database};UID={db_user};PWD={db_password}"

    try:
        connection = pyodbc.connect(conn_str)
        print("Successfully connected to the database")
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None

def create_table(connection):
    """ Create a table if it doesn't already exist. """
    cursor = connection.cursor()
    create_table_query = """
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='users' AND xtype='U')
    CREATE TABLE users (
        id INT IDENTITY(1,1) PRIMARY KEY,
        name NVARCHAR(100) NOT NULL,
        age INT NOT NULL
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully.")

def insert_user(connection, name, age):
    """ Insert a new user into the users table. """
    cursor = connection.cursor()
    insert_query = "INSERT INTO users (name, age) VALUES (?, ?);"
    cursor.execute(insert_query, (name, age))
    connection.commit()
    print(f"User {name} inserted with age {age}.")

def retrieve_users(connection):
    """ Retrieve and print all users from the users table. """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()

    print("Users:")
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}")

def main():
    connection = create_connection()
    if connection:
        create_table(connection)
        insert_user(connection, "Alice", 30)
        insert_user(connection, "Bob", 25)
        retrieve_users(connection)
        connection.close()

if __name__ == "__main__":
    main()
