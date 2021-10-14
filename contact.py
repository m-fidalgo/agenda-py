class Contact():
  def __init__(self, nome=None, idade=None, tel=None, id=None):
    self.__nome = nome
    self.__idade = idade
    self.__tel = tel
    self.__id = id

  @property
  def nome(self):
    return self.__nome

  @property
  def idade(self):
    return self.__idade

  @property
  def tel(self):
    return self.__tel

  @property
  def id(self):
    return self.__id

  @nome.setter
  def nome(self, nome):
    self.__nome = nome

  @idade.setter
  def idade(self, idade):
    self.__idade = idade

  @tel.setter
  def tel(self, tel):
    self.__tel = tel
  
  @id.setter
  def id(self, id):
    self.__id = id