import sys
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database

if len(sys.argv) != 6:
    print("Usage: python create_db.py <PG_NAME> <PG_HOST> <PG_PORT> <PG_USER> <PG_PASSWORD>")
    sys.exit(1)

PG_NAME = sys.argv[1]
PG_HOST = sys.argv[2]
PG_PORT = sys.argv[3]
PG_USER = sys.argv[4]
PG_PASSWORD = sys.argv[5]

dsn = "postgresql://{user}:{password}@{host}:{port}/{db_name}".format(
    user=PG_USER,
    password=PG_PASSWORD,
    host=PG_HOST,
    port=PG_PORT,
    db_name='aabbccdd'
)

engine = create_engine(dsn)
create_database(engine.url)
