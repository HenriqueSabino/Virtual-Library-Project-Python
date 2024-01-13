# config/settings.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "mssql+pyodbc://username:password@server/database?driver=ODBC+Driver+17+for+SQL+Server"
    default_loan_duration_days: int = 14  # Example default setting

    class Config:
        env_file = ".env"

settings = Settings()