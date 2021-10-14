from factories.connection_factory import ConnectionFactory
from entities.contact import Contact

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
  def find_by_id(id):
    db = ConnectionFactory.connect()
    try:
      cursor = db.cursor()
      cursor.execute("SELECT * FROM contatos WHERE id=%s", (id, ))
      res = cursor.fetchone()
      if len(res) != 0:
        return Contact(res[1], res[2], res[3], res[0])
      return False
    finally:
      db.close()

  @staticmethod
  def export_contacts():
    try:
      with open("agenda.txt","w") as file:
        agenda = ContactRepository.get()
        for c in agenda:
          file.write(f"{c.id} - {c.nome} - {c.idade} - {c.tel} \n")
    except FileNotFoundError:
      print("Arquivo não encontrado")

  @staticmethod
  def import_contacts():
    try:
      with open("agenda.txt", "r") as file:
        linhas = file.readlines()
        for linha in linhas:
          dados = linha.split(" - ")
          ContactRepository.insert(Contact(dados[1], int(dados[2]), dados[3].split(" \n")[0]))
    except FileNotFoundError:
      print("Arquivo não encontrado")