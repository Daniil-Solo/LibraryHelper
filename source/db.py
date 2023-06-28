import psycopg2
import json


def get_db_data(path: str) -> dict[str:str]:
    with open(path, "r") as f:
        config = json.load(f)
    return config["db"]


def get_connection():
    """
    Получение сессии базы данных
    """
    db_data = get_db_data("config.json")
    conn = psycopg2.connect(
        **db_data
    )
    return conn


class ConnectionContextManager:
    def __init__(self):
        self.conn = None

    def __enter__(self):
        self.conn = get_connection()
        return self.conn

    def __exit__(self, exp_type, exp_value, traceback):
        if self.conn:
            self.conn.close()