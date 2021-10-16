from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from factories.connection_factory import ConnectionFactory

cf = ConnectionFactory()
engine = cf.connect()

Base = declarative_base()

class TableContact(Base):
  __tablename__ = 'contatos'
  id = Column(Integer, primary_key=True)
  nome = Column(String(200), nullable=False)
  idade = Column(Integer, nullable=False)
  tel = Column(String(12), nullable=False)

  def __repr__(self):
    return "Contato %s ('%s', '%s', '%s')" % (self.id, self.nome, self.idade, self.tel)

Base.metadata.create_all(engine)