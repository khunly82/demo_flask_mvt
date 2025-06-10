SECRET_KEY = 'l0-yh=@v8cn2r*cvn5^-elmmp&o=4k5x3+3q49yjg)cr1u4xrh'

scheme = 'postgresql+psycopg2'
username = 'qrufxnufbb'
password = 'lwZaGxsW4knwS$1b'
host_name = 'testkhunflask-server'
port = '5432'
database_name = 'testkhunflask-database'

URL_DB = f"{scheme}://{username}:{password}@{host_name}:{port}/{database_name}"

SQLALCHEMY_DATABASE_URI = URL_DB