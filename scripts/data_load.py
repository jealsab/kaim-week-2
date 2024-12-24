import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def load_data_from_postgres(query):
    """Connect to PostgreSQL using SQLAlchemy, execute query, and load data into a pandas DataFrame."""
    try:
        # Create the SQLAlchemy engine for PostgreSQL
        engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        
        # Use pandas to execute the query and return the DataFrame
        df = pd.read_sql_query(query, engine)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to execute a query and return the result as a DataFrame
def aggregate_xdr_data():
    query = """
    SELECT 
        "IMSI" AS user_id,
        COUNT(*) AS number_of_sessions,
        SUM("Dur. (ms)") AS total_session_duration,
        SUM("Total DL (Bytes)") AS total_download_data,
        SUM("Total UL (Bytes)") AS total_upload_data,
        SUM(
            COALESCE("Total DL (Bytes)", 0) + 
            COALESCE("Total UL (Bytes)", 0)
        ) AS Total_Data_Volume
    FROM 
        xdr_data
    GROUP BY 
        "IMSI";
    """
    return load_data_from_postgres(query)
