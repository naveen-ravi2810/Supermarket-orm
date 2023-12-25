from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
import os
from dotenv import load_dotenv
load_dotenv()

Base = declarative_base()

sql_path = os.getenv('database_uri')
engine = create_engine(sql_path, echo=True)

# Session = sessionmaker(bind=engine)
# session = Session()
session = scoped_session(
    sessionmaker(
        autoflush=False,
        autocommit=False,
        bind=engine
    )
)

Base.query = session.query_property()
