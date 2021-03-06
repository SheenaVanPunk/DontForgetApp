import mysql.connector


class Database:
    def __init__(self):
        self._db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="todo_db"
        )
        self._cursor = self._db.cursor()

    def get_db_connection(self):
        return self._db

    def get_cursor(self):
        return self._cursor

    def commit(self):
        self.get_db_connection().commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.get_db_connection().close()

    def execute(self, sql, params=None):
        self.get_cursor().execute(sql, params or ())

    def fetchall_results(self, sql, params=None):
        self.get_cursor().execute(sql, params or ())
        return self.get_cursor().fetchall()

    def fetchone_result(self, sql, params=None):
        self.get_cursor().execute(sql, params or ())
        results = self.get_cursor().fetchone()
        self.get_db_connection().close()
        return results

    def query_db(self, sql, params=None):
        self.get_cursor().execute(sql, params or ())
        results = self.get_cursor().fetchall()
        self.get_db_connection().close()
        return results

    def commit_to_db(self, sql, params=None):
        self.get_cursor().execute(sql, params or ())
        self.get_db_connection().commit()
        self.get_db_connection().close()

