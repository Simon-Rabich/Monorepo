# For local run (also tests run).
BASIC_CONFIG = {
    # "DB_URL": 'postgresql' + '+psycopg2' + '://' + 'admin:admin@localhost:5432/parking_decision',
    "DB_URL": "postgresql+pg8000://root:root@localhost:5432/feedgate",

    "WEB_HOST": "0.0.0.0",
    "WEB_PORT": 8000
}
