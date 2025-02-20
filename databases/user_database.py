import sqlite3
import logging
from datetime import datetime
from tabulate import tabulate


class user_database:
    def __init__(self, db_name="users.db"):
        self.db_name = db_name
        self._init_database()

    def _execute(self, query, params=(), fetchone=False, fetchall=False):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
                if fetchone:
                    return cursor.fetchone()
                if fetchall:
                    return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
        return None

    def _init_database(self):
        query = '''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            username TEXT,
            language_code TEXT,
            is_premium BOOLEAN,
            chat_id INTEGER,
            chat_type TEXT,
            joined_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        '''
        self._execute(query)
        logging.info("Database initialized.")

    def add_user(self, user_id: int, first_name: str, last_name: str, username: str,
                 language_code: str, is_premium: bool, chat_id: int, chat_type: str):
        if self._execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,), fetchone=True):
            logging.info(f"User {user_id} already exists.")
            return

        query = '''
        INSERT INTO users (user_id, first_name, last_name, username, language_code, is_premium, chat_id, chat_type, joined_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        self._execute(query, (user_id, first_name, last_name, username, language_code,
                              is_premium, chat_id, chat_type, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        logging.info(f"User {user_id} added.")

    def get_users_table(self):
        users = self._execute("SELECT * FROM users", fetchall=True)
        headers = ["User ID", "First Name", "Last Name", "Username", "Language", "Premium", "Chat ID", "Chat Type",
                   "Joined At"]
        return tabulate(users, headers=headers, tablefmt="grid") if users else "No users found."

    def get_user(self, user_id: int):
        return self._execute("SELECT * FROM users WHERE user_id = ?", (user_id,), fetchone=True)

    def delete_user(self, user_id: int):
        if self._execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,), fetchone=True):
            self._execute("DELETE FROM users WHERE user_id = ?", (user_id,))
            logging.info(f"User {user_id} deleted.")
        else:
            logging.info(f"User {user_id} not found.")

    def count_users(self):
        count = self._execute("SELECT COUNT(*) FROM users", fetchone=True)
        return count[0] if count else 0


db = user_database()
