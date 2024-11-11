import os


user = os.getenv('PGUSER')
password = os.getenv('PGPASSWORD')
host = os.getenv('PGHOST')
database = os.getenv('DATABASE')
DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"
