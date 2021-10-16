from queries.contact_query import ContactQuery
from entities.contact import Contact
from domains.db import TableContact

class ContactRepository():
  def get(self, session):
    contact_query = ContactQuery()
    agenda_tabela = contact_query.get(session)
    agenda = []

    for c in agenda_tabela:
      agenda.append(Contact(c.nome, c.idade, c.tel, c.id))
    
    return agenda

  def insert(self, contato, session):
    contact_query = ContactQuery()
    new_contact = TableContact(nome=contato.nome,idade=contato.idade, tel=contato.tel)
    contact_query.insert(new_contact, session)

  def update(self, id, contato, session):
    contact_query = ContactQuery()
    contact_query.update(id, contato, session)

  def delete(self, id, session):
    contact_query = ContactQuery()
    contact_query.delete(id, session)

  def export_contacts(self, session):
    try:
      with open("agenda.txt","w") as file:
        agenda = self.get(session)
        for c in agenda:
          file.write(f"{c.id} - {c.nome} - {c.idade} - {c.tel} \n")
    except FileNotFoundError:
      print("Arquivo não encontrado")

  def import_contacts(self, session):
    try:
      with open("agenda.txt", "r") as file:
        linhas = file.readlines()
        for linha in linhas:
          dados = linha.split(" - ")
          contato = Contact(dados[1], int(dados[2]), dados[3].split(" \n")[0])
          self.insert(contato, session)
    except FileNotFoundError:
      print("Arquivo não encontrado")