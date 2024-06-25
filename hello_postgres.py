from sqlalchemy import create_engine
import psycopg2
import pandas as pd 

# credentials
username = 'citizix_user'
password = 'S3cret'
host = 'localhost'
port = 5432
database = 'citizix_db'

# Create the connection string
connection_string = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'

# Create the engine
engine = create_engine(connection_string)

def create_table(file_name, table_name):
    # read data from a csv, sanitize the column names and insert into postgres

    df = pd.read_csv(file_name)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('.','_').str.replace('/','').str.replace('&','_n_')

    # Create/Refresh Postgres tables
    df.to_sql(table_name, engine, schema='public', if_exists = 'replace', index=False)
    # df.to_sql(table_name, engine, schema='public', if_exists = 'append', index=False)

def get_data(query):
    # Execute the query and store results in a DataFrame

    # query = "SELECT * FROM public.sample_data"
    df = pd.read_sql_query(query, engine)
    print(df)

if __name__ == "__main__":
    create_table(file_name='./sample_data/sample_data.csv', table_name='sample_data')
    get_data(query="SELECT * FROM public.sample_data")