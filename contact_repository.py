from connection_factory import ConnectionFactory
from contact import Contact

class ContactRepository():
  @staticmethod
  def get():
    db = ConnectionFactory.connect()
    agenda = []
    try:
      cursor = db.cursor()
      cursor.execute("SELECT * FROM contatos")
      
      for i in cursor.fetchall():
        agenda.append(Contact(i[1], int(i[2]), i[3], int(i[0])))
    finally:
      db.close()
      return agenda

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

  @staticmethod
  def find_by_name(nome):
    db = ConnectionFactory.connect()
    try:
      cursor = db.cursor()
      print(nome)
      cursor.execute("SELECT tel FROM contatos WHERE nome=%s", (nome,))
      res = cursor.fetchone()
      if len(res) != 0:
        return res[0]
      return False
    finally:
      db.close()

  @staticmethod
  def find_id(id):
    db = ConnectionFactory.connect()
    try:
      cursor = db.cursor()
      cursor.execute("SELECT id FROM contatos WHERE id=%s", (id, ))
      
      if cursor.fetchone():
        return True
      return False
    finally:
      db.close()