"""
Created db backup if the db is offline 
"""
import contextlib

class DBHandler:

    def __init__(self, value):
        print(value)

    def make_backup(self):
        print('creating backup....')

    def __enter__(self):
        self.stop_db()
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.restart_db()

    def stop_db(self):
        print('stop database')

    def restart_db(self):
        print('restarting database ...')


with DBHandler('es un dato al init') as db:
    db.make_backup()
   

print('=='*30)

@contextlib.contextmanager
def db_handler():
    try:
        db =  DBHandler('desde decorador')
        db.stop_db()
        yield
    finally:
        db.restart_db()


with db_handler():
    print('hace algo con la db')