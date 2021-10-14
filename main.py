from contact import Contact
from contact_repository import ContactRepository

menu = 1

while menu != 0:
  print("-- AGENDA --")
  print("1. Listar Contatos")
  print("2. Inserir Contato")
  print("3. Atualizar Contato")
  print("4. Remover Contato")
  print("5. Buscar Contato")
  print("0. Sair")

  menu = int(input("Opção: "))

  if menu == 1:
    agenda = ContactRepository.get()
    for c in agenda:
      print(f"{c.id} - {c.nome} - {c.idade} anos - Tel: {c.tel}")
  elif menu == 2:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    tel = input("Telefone: ")
    ContactRepository.insert(Contact(nome, idade, tel))
  elif menu == 3:
    id = int(input("Id: "))
    if ContactRepository.find_id(id):
      nome = input("Nome: ")
      idade = int(input("Idade: "))
      tel = input("Telefone: ")
      ContactRepository.update(id, Contact(nome, idade, tel))
    else:
      print("Id não encontrado")
  elif menu == 4:
    id = int(input("Id: "))
    if ContactRepository.find_id(id):
      ContactRepository.delete(id)
    else:
      print("Id não encontrado")
  elif menu == 5:
    nome = input("Nome: ")
    tel = ContactRepository.find_by_name(nome)
    if tel:
      print(f"Telefone: {tel}")
    else:
      print("Contato não encontrado")
  else:
    print("Opção inválida")
