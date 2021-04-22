from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Database():
    def __init__(self):
        self.engine = create_engine('sqlite+pysqlite:///:memory:', future=True)
        self.session = scoped_session(sessionmaker(autocommit=False,
                                                autoflush=False,
                                                bind=self.engine))
        self.Base = declarative_base()
        self.Base.query = self.session.query_property()


# Database singleton
db = Database()
