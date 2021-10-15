import MySQLdb, configparser

class ConnectionFactory():
  def connect(self):
    config = configparser.ConfigParser()
    config.read('config.ini')
    db = MySQLdb.connect(user=config['DB']['user'],
                        passwd=config['DB']['password'],
                        db=config['DB']['db'],
                        host=config['DB']['host'],
                        port=int(config['DB']['port']),
                        autocommit=config['DB']['autocommit'])
    return db