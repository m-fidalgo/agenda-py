import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ConnectionFactory():
  def connect(self):
    config = configparser.ConfigParser()
    config.read('./config.ini')
    user = config['DB']['user']
    password = config['DB']['password']
    db = config['DB']['db']
    host = config['DB']['host']
    port = config['DB']['port']

    engine = create_engine(f"mysql://{user}:{password}@{host}:{port}/{db}")
    return engine

  def create_session(self):
    connection = self.connect()
    Session = sessionmaker()
    Session.configure(bind=connection)
    session = Session()
    return session