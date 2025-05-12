import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv(dotenv_path="/Users/patrickanderson/Desktop/DACSS 690A/690A Final/.env")

def load_data_to_postgres(df, table_name):
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    db = os.getenv('DB_NAME')

    db_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
    engine = create_engine(db_url)

    try:
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Data successfully loaded into table '{table_name}'.")
    except Exception as e:
        print(f"Failed to load data: {e}")



