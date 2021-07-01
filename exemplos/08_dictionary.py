#criando um DICTIONARY
contatos = {'Yan': '(41) 1234-5678',
            'Pedro': ' (41) 9999-9999',
            'Ana': '(41) 8765-4321',
            'Marina': '(41) 8877-7788'}

#acessando um valor
print(contatos['Yan'])

#outra forma de acessar
print(contatos.get("Yan"))

#alterar um valor
contatos['Yan'] = "(41) 9 1234-5678"
print("Contato Yan alterado: ", contatos['Yan'])

#outra forma de alterar um valor
contatos.update({"Pedro" : "(41) 9 8888-8888"})
print("Contato Pedro alterado: ", contatos['Pedro'])

#adicionando um item
contatos["Cicrano"] = "(41) 9 1234-6789"

#outra forma de adicionar um número
contatos.update({"Fulano" : "(41) 9 9876-5432"})

#remover um item
contatos.pop("Ana")

print("Todos os contatos:")
print(contatos)