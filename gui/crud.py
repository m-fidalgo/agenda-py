from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup
from kivy.properties import partial

from repositories.contact_repository import ContactRepository
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
    self.text = self.nome_contato + " " + str(self.idade_contato) + " " + self.tel_contato
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
    contactRep = ContactRepository()
    agenda = contactRep.get()

    for contato in agenda:
      self.ids.agenda.add_widget(ContactBtn(contato))

  def insert(self):
    if self.__verify_fields():
      nome = self.ids.nome.text
      idade = int(self.ids.idade.text)
      tel = self.ids.tel.text
      contactRep = ContactRepository()
      contactRep.insert(Contact(nome, idade, tel))
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
      contactRep = ContactRepository()
      contactRep.update(id, Contact(nome, idade, tel))
      self.__clean_fields()
      self.get()

  def delete(self):
    id = MainScreen.selected_id
    popup = DeletePopUp()
    popup.delete_function = partial(self.delete_contact, id)
    popup.open()

  def delete_contact(self, id):
    contactRep = ContactRepository()
    contactRep.delete(id)
    MainScreen.selected_id = 0
    self.__clean_fields()
    self.get()

  def export_contacts(self):
    contactRep = ContactRepository()
    contactRep.export_contacts()

  def import_contacts(self):
    contactRep = ContactRepository()
    contactRep.import_contacts()
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
