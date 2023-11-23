agenda = {}
while True:
    print('--- AGENDA TELEFÔNICA ---')
    print('1 - Adicionar contato')
    print('2 - Editar telefone')
    print('3 - Remover contato')
    print('4 - Buscar contato')
    print('5 - Listar todos')
    print('6 - Sair')
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        nome = input('Digite o nome do contato: ')
        if nome not in agenda:
            agenda[nome] = input(f'Digite o telefone de {nome}: ')
            print('Contato adicionado com sucesso!')
        else:
            print('Já existe um contato com esse nome!')

    elif opcao == 2:
        nome = input('Digite o nome do contato: ')
        if nome in agenda:
            agenda[nome] = input(f'Digite o novo telefone de {nome}: ')
            print('Telefone editado com sucesso!')
            print(agenda)
        else:
            print('Contato não encontrado!')

    elif opcao == 3:
        nome = input('Digite o nome do contato: ')
        if nome in agenda:
            del agenda[nome]
            print('Contato removido com sucesso!')
            print(agenda)
        else:
            print('Contato não encontrado!')

    elif opcao == 4:
        nome = input('Digite o nome do contato: ')
        if nome in agenda:
            print(f'Telefone: {agenda[nome]}')
        else:
            print('Contato não encontrato!')
    elif opcao == 5:
        print('--- Todos os contatos ---')
        for key in agenda:
            print(f'Nome: {key} - Telefone: {agenda[key]}')
    elif opcao == 6:
        print('Você saiu do programa')
        break
    else:
        print('Opção inválida!')