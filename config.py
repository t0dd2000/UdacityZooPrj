import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'databasesqlwestttn.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'database-west'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'ttndbadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'admin123!'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'ttnstorageacct'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'R6mN9tjDLoGHRCWHw/GP7ODWtMNn3+voTDU8x/JdC912VNrHU44eJVue8fgc/iwLsmEYzZ4HgPkEN3LLma+4+g=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'ttnstoragecontainer'

