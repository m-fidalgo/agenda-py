from domains.db import TableContact

class ContactQuery():
  def get(self, session):
    agenda = session.query(TableContact).all()
    return agenda

  def insert(self, contact, session):
    session.add(contact)
  
  def update(self, id, contact, session):
    contato = self.get_by_id(id, session)
    contato.nome = contact.nome
    contato.idade = contact.idade
    contato.tel = contact.tel
    #session.query(TableContact).filter(TableContact.id == id).update({'nome': contact.nome, 'idade': contact.idade, 'tel': contact.tel})

  def delete(self, id, session):
    contato = self.get_by_id(id, session)
    session.delete(contato)

  def get_by_id(self, id, session):
    contato = session.query(TableContact).filter(TableContact.id == id).one()
    return contato
