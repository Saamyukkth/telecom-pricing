import pandas as pd
from sqlalchemy import create_engine

def load_data(db_connection_string):
    engine = create_engine(db_connection_string)
    customer_data = pd.read_sql('SELECT * FROM customer_usage', engine)
    pricing_data = pd.read_sql('SELECT * FROM pricing_history', engine)
    competitor_data = pd.read_sql('SELECT * FROM competitor_pricing', engine)
    return customer_data, pricing_data, competitor_data

def preprocess_customer_usage(df):
    df['month'] = pd.to_datetime(df['month'])
    df.fillna(0, inplace=True)
    df['total_usage'] = df['data_usage'] + df['call_usage']
    return df
