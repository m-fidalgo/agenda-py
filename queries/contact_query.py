from domains.db import TableContact

class ContactQuery():
  def get(self, session):
    agenda = session.query(TableContact).all()
    return agenda

  def insert(self, contact, session):
    session.add(contact)
  
  def update(self, id, contact, session):
    session.query(TableContact).filter(TableContact.id == id).update({'nome': contact.nome, 'idade': contact.idade, 'tel': contact.tel})

  def delete(self, id, session):
    contato = session.query(TableContact).filter(TableContact.id == id).one()
    session.delete(contato)
