#Singleton class that connects to a local database and returns a cursor that you can use for querying
#The local MySql Database's name is 'mydb' and it contains already one table named 'post'

import mysql.connector

class Connection(object):
    class __Connection:
        def __init__(self):
            self.conn = mysql.connector.connect(user='root', password='Kamorio2$', host='127.0.0.1', database='mydb')
            self.cursor = self.conn.cursor()
    instance = None
    def __new__(cls):
        if not Connection.instance:
            Connection.instance = Connection.__Connection()
        return Connection.instance



