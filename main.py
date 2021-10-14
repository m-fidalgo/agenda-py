from typing import final
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
  print("6. Exportar Contatos")
  print("7. Importar Contatos")
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
  elif menu == 6:
    try:
      with open("agenda.txt","a") as file:
        agenda = ContactRepository.get()
        for c in agenda:
          file.write(f"{c.id} - {c.nome} - {c.idade} - {c.tel} \n")
    except FileNotFoundError:
      print("Arquivo não encontrado")
  elif menu == 7:
    try:
      with open("agenda.txt", "r") as file:
        linhas = file.readlines()
        for linha in linhas:
          dados = linha.split(" - ")
          ContactRepository.insert(Contact(dados[1], int(dados[2]), dados[3].split(" \n")[0]))
    except FileNotFoundError:
      print("Arquivo não encontrado")
  elif menu == 0:
    print("Saindo...")
  else:
    print("Opção inválida")
