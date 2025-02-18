from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self):
        self.__connetion_string = "sqlite:////home/caio/github-repositories/pessoal/dev-stage/python/db/schema.db"
        self.__engine = self.__create_database_engine()
        self.session = None
        
    def __create_database_engine(self):
        engine = create_engine(self.__connetion_string)
        return engine
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()