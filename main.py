from contact import Contact
from contact_repository import ContactRepository

menu = 1

while menu != 0:
  print("-- AGENDA --")
  print("1. Listar Contatos")
  print("2. Inserir Contato")
  print("3. Atualizar Contato")
  print("4. Remover Contato")
  print("0. Sair")

  menu = int(input("Opção: "))

  if menu == 1:
    ContactRepository.get()
  elif menu == 2:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    tel = input("Telefone: ")
    ContactRepository.insert(Contact(nome, idade, tel))
  elif menu == 3:
    id = int(input("Id: "))
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    tel = input("Telefone: ")
    ContactRepository.update(id, Contact(nome, idade, tel))
  elif menu == 4:
    id = int(input("Id: "))
    ContactRepository.delete(id)
  else:
    print("Opção inválida")
