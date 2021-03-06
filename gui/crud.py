from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup
from kivy.properties import partial

from repositories.contact_repository import ContactRepository
from factories.connection_factory import ConnectionFactory
from entities.contact import Contact

class DeletePopUp(Popup):
  pass

class MsgPopUp(Popup):
  pass

class ContactBtn(ToggleButton):  
  def __init__(self, contato, **kwargs):
    super(ContactBtn, self).__init__(**kwargs)
    self.id_contato = contato.id
    self.nome_contato = contato.nome
    self.idade_contato = contato.idade
    self.tel_contato = contato.tel
    self.text = f"{self.nome_contato} {self.idade_contato} {self.tel_contato}"
    self.group = 'contatos'

  def _do_release(self, *args):
    MainScreen().select_contact(self.id_contato)

class MainScreen(BoxLayout):
  selected_id = 0

  def __init__(self, **kwargs):
    super(MainScreen, self).__init__(**kwargs)
    self.get()
  
  def get(self):
    self.ids.agenda.clear_widgets()
    connectionFactory = ConnectionFactory()
    session = connectionFactory.create_session()
    try:
      contactRep = ContactRepository()
      agenda = contactRep.get(session)

      for contato in agenda:
        self.ids.agenda.add_widget(ContactBtn(contato))
    except:
      session.rollback()
      raise
    finally:
      session.close()

  def insert(self):
    if self.__verify_fields():
      nome = self.ids.nome.text
      idade = int(self.ids.idade.text)
      tel = self.ids.tel.text
      connectionFactory = ConnectionFactory()
      session = connectionFactory.create_session()
      try:
        contactRep = ContactRepository()
        contactRep.insert(Contact(nome, idade, tel), session)
        session.commit()
      except:
        session.rollback()
        raise
      finally:
        session.close()
      self.__clean_fields()
      self.get()

  def select_contact(self, id):
    MainScreen.selected_id = id

  def update(self):
    if self.__verify_fields():
      id = MainScreen.selected_id
      nome = self.ids.nome.text
      idade = int(self.ids.idade.text)
      tel = self.ids.tel.text
      connectionFactory = ConnectionFactory()
      session = connectionFactory.create_session()
      try:
        contactRep = ContactRepository()
        contactRep.update(id, Contact(nome, idade, tel), session)
        session.commit()
      except:
        session.rollback()
        raise
      finally:
        session.close()
      self.__clean_fields()
      self.get()

  def delete(self):
    id = MainScreen.selected_id
    popup = DeletePopUp()
    popup.delete_function = partial(self.delete_contact, id)
    popup.open()

  def delete_contact(self, id):
    connectionFactory = ConnectionFactory()
    session = connectionFactory.create_session()
    try:
      contactRep = ContactRepository()
      contactRep.delete(id, session)
      session.commit()
    except:
      session.rollback()
      raise
    finally:
      session.close()
    MainScreen.selected_id = 0
    self.__clean_fields()
    self.get()

  def export_contacts(self):
    connectionFactory = ConnectionFactory()
    session = connectionFactory.create_session()
    try:
      contactRep = ContactRepository()
      contactRep.export_contacts(session)
    except:
      session.rollback()
      raise
    finally:
      session.close()

  def import_contacts(self):
    connectionFactory = ConnectionFactory()
    session = connectionFactory.create_session()
    try:
      contactRep = ContactRepository()
      contactRep.import_contacts(session)
      session.commit()
    except:
      session.rollback()
      raise
    finally:
      session.close()
    
    self.get()

  def __clean_fields(self):
    self.ids.nome.text = ""
    self.ids.idade.text = ""
    self.ids.tel.text = ""

  def __verify_fields(self):
    if self.ids.nome.text == "" or self.ids.idade.text == "" or self.ids.tel.text == "":
      MsgPopUp().open()
      return False
    return True

class Crud(App):
  def build(self):
    return MainScreen()
