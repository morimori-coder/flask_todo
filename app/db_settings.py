from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import pyodbc

# Create the engine
SERVER = "172.25.0.2"
DATABASE = "todoapp"
USERNAME = "sa"
PASSWORD = "saPassword1234"
connectionString = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}"
# conn = pyodbc.connect(connectionString)

engine = create_engine(connectionString, encoding="utf-8", echo=True)

# Create a session factory
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()
