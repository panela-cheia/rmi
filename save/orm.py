from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from save.schema import Base

class ORM:
    def __init__(self):
        self.engine = create_engine('sqlite:///dev.db')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        
    def create_tables(self):
        Base.metadata.create_all(self.engine)
        print("Tabelas criadas com sucesso!")

    def get_session(self):
        return self.session