from sqlalchemy import create_engine
from schema import Base

# Crie o engine de conexão com o banco de dados
engine = create_engine('sqlite:///dev.db')

# Crie as tabelas no banco de dados
Base.metadata.create_all(engine)

print("Banco de dados criado com sucesso!")