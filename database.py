import sqlite3
import hashlib
import uuid
from datetime import datetime


class Database:
    def __init__(self):
        self.con = sqlite3.connect('knowledge_base.db')
        self.cursor = self.con.cursor()
        self.create_task_table()
        self.create_user_table()

    def create_task_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS tasks(id integer PRIMARY KEY AUTOINCREMENT, "
            "entry_date DATE, "
            "user_id integer, "
            "reading_type varchar(50), "
            "bgl_reading varchar(50), "
            "meal_taken varchar(50)"
            ")"
        )
        self.con.commit()

    def create_user_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY AUTOINCREMENT, "
            "user_id integer, "
            "username varchar(50) UNIQUE NOT NULL, "
            "password_hash varchar(100) NOT NULL)"
        )
        self.con.commit()

    def register_user(self, username, password):
        try:
            user_ids = str(uuid.uuid4())

            password_hash = hashlib.sha256(password.encode()).hexdigest()

            sql = "INSERT INTO users (user_id, username, password_hash) VALUES (?, ?, ?)"
            self.cursor.execute(sql, (user_ids, username, password_hash))
            self.con.commit()
            print(f"Successfully registered user: {username} with user ID: {user_ids}")
        except sqlite3.IntegrityError:
            print(f"User '{username}' already exists.")
        except sqlite3.Error as e:
            print(f"SQLite error: {str(e)}")
        except Exception as e:
            print(f"Error registering user: {str(e)}")

    def authenticate_user(self, username, password):
        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            current_datetime = datetime.now()
            entry_date = current_datetime.date()

            sql = "SELECT user_id FROM users WHERE username = ? AND password_hash = ?"
            self.cursor.execute(sql, (username, password_hash))
            user_id = self.cursor.fetchone()

            if user_id:
                user_id = user_id[0]
                print('entry_date: ', entry_date)
                print('user_id: ', user_id)

                sql = "INSERT INTO tasks (entry_date, user_id) VALUES (?, ?)"
                self.cursor.execute(sql, (entry_date, user_id))
                self.con.commit()
                print(f"Login successful. User '{username}' logged in and task updated.")
                return True
            else:
                print("Login failed. Invalid username or password.")
                return False
        except sqlite3.Error as e:
            print(f"SQLite error: {str(e)}")
        except Exception as e:
            print(f"Error logging in: {str(e)}")

    def insert_reading_type(self, reading_type):
        try:
            sql = "UPDATE tasks SET reading_type = ? WHERE reading_type IS NULL AND bgl_reading IS NULL"

            self.cursor.execute(sql, (reading_type,))
            self.con.commit()
            print(f"Successfully inserted '{reading_type}' into reading_type column.")
        except sqlite3.Error as e:
            print(f"SQLite error: {str(e)}")
        except Exception as e:
            print(f"Error inserting data into reading_type column: {str(e)}")

    def insert_bgl_reading(self, bgl_reading):
        try:
            sql = "UPDATE tasks SET bgl_reading = ? WHERE reading_type IS NOT NULL AND bgl_reading IS NULL"
            self.cursor.execute(sql, (bgl_reading,))
            self.con.commit()
            print(f"Successfully inserted '{bgl_reading}' into bgl_reading column.")
        except sqlite3.Error as e:
            print(f"SQLite error: {str(e)}")
        except Exception as e:
            print(f"Error inserting data into bgl_reading column: {str(e)}")

    def insert_meal_taken(self, meal_taken):
        try:
            sql = "UPDATE tasks SET meal_taken = ? WHERE reading_type IS NOT NULL AND bgl_reading IS NOT NULL AND meal_taken IS NULL"
            self.cursor.execute(sql, (meal_taken,))
            self.con.commit()
            print(f"Successfully inserted '{meal_taken}' into meal_taken column.")
        except sqlite3.Error as e:
            print(f"SQLite error: {str(e)}")
        except Exception as e:
            print(f"Error inserting data into meal_taken column: {str(e)}")

    def get_last_entry(self, column_name):
        try:
            sql = f"SELECT {column_name} FROM tasks WHERE {column_name} IS NOT NULL ORDER BY id DESC LIMIT 1"
            result = self.cursor.execute(sql).fetchone()
            if result:
                return result[0]
            else:
                return None
        except sqlite3.Error as e:
            print(f"SQLite error: {str(e)}")
        except Exception as e:
            print(f"Error retrieving data from {column_name} column: {str(e)}")

    def get_second_last_entry(self, column_name):
        try:
            sql = f"SELECT {column_name} FROM tasks WHERE {column_name} IS NOT NULL ORDER BY id DESC LIMIT 1 OFFSET 1"
            result = self.cursor.execute(sql).fetchone()
            if result:
                return result[0]
            else:
                return None
        except sqlite3.Error as e:
            print(f"SQLite error: {str(e)}")
        except Exception as e:
            print(f"Error retrieving data from {column_name} column: {str(e)}")

    def get_secondary_column(self, primary_column, secondary_column):
        try:
            sql = f"SELECT {primary_column}, {secondary_column} FROM tasks WHERE {primary_column} IS NOT NULL ORDER BY id DESC LIMIT 1"
            result = self.cursor.execute(sql).fetchone()
            if result:
                return result
            else:
                return None
        except sqlite3.Error as e:
            print(f"SQLite error: {str(e)}")
        except Exception as e:
            print(f"Error retrieving data from {primary_column} and {secondary_column} columns: {str(e)}")

    def retrieve_data_from_database(self):
        self.cursor.execute("SELECT * FROM tasks")
        tasks = self.cursor.fetchall()
        return tasks


    def close_db_connection(self):
        self.con.close()
