from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib

# Define the parameters for the database connection here
DATABASE_URL = "mssql+pyodbc://username:password@host:port/database_name?driver=ODBC+Driver+17+for+SQL+Server"

# Encode the URL to be compatible with ODBC connections
params = urllib.parse.quote_plus(DATABASE_URL)

# Create the engine, which the Session will use for connection resources
engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()