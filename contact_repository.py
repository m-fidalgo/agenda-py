from connection_factory import ConnectionFactory
from contact import Contact

class ContactRepository():
  @staticmethod
  def get():
    db = ConnectionFactory.connect()
    try:
      cursor = db.cursor()
      cursor.execute("SELECT * FROM contatos")
      
      for i in cursor.fetchall():
        print(f"{i[0]} - {i[1]} - {i[2]} anos - Telefone: {i[3]}")
    finally:
      db.close()

  @staticmethod
  def insert(contato):
    db = ConnectionFactory.connect()
    try:
      cursor = db.cursor()
      cursor.execute("INSERT INTO contatos (nome, idade, tel) VALUES (%s, %s, %s)", (contato.nome, contato.idade, contato.tel))
    finally:
      db.close()

  @staticmethod
  def update(id, contato):
    db = ConnectionFactory.connect()
    try:
      cursor = db.cursor()
      cursor.execute("UPDATE contatos SET nome=%s, idade=%s, tel=%s WHERE id=%s", (contato.nome, contato.idade, contato.tel, id))
    finally:
      db.close()

  @staticmethod
  def delete(id):
    db = ConnectionFactory.connect()
    try:
      cursor = db.cursor()
      cursor.execute("DELETE FROM contatos WHERE id=%s", (id, ))
    finally:
      db.close()