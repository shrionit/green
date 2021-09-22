from sqlalchemy import create_engine as Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app import settings


def postgres_dblink_gen(settings):
    db = settings.DATABASE
    return f"postgresql://{db['DBUSER']}:{db['DBPASS']}@{db['DBHOST']}:{db['DBPORT']}/{db['DBNAME']}"

dblink = postgres_dblink_gen(settings)

engine = Engine(dblink)
Session = sessionmaker(bind=engine)
Base = declarative_base()