from sqlalchemy import create_engine

def get_db_connection(db_connection_string):
    return create_engine(db_connection_string)
