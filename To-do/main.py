from time import sleep

lista_de_tarefas = []
lista_de_tarefas_completadas = []


# definindo as cores usadas no terminal
cor_texto_azul = '\033[1;34m'
cor_texto_verde = '\033[1;32m'
cor_texto_vermelho = '\033[1;31m'
cor_texto_amarelo = '\033[1;33m'
cor_texto_ciano = '\033[1;36m'
cor_background_azul = '\033[1;44m'
# definindo o fechamento 
fechamento = '\033[m'

while True:
    sleep(0.5)

    print(f'\n{cor_texto_azul}{cor_background_azul}Menu do Gerenciador de Tarefas{fechamento} :')
    print(f'''
    1. {cor_texto_verde}Adicionar Tarefa{fechamento}
    2. {cor_texto_ciano}Ver Tarefas{fechamento}
    3. {cor_texto_verde}Atualizar Tarefas{fechamento}
    4. {cor_texto_amarelo}Completar Tarefa{fechamento}
    5. {cor_texto_amarelo}Deletar Tarefas Completadas{fechamento}
    6. {cor_texto_vermelho}Sair{fechamento}
    ''')

    escolha = (input(f'{cor_background_azul}Digite sua Escolha{fechamento} : '))

    if escolha == '1':
        novaTarefa = input(f'{cor_background_azul}Adicione a tarefa{fechamento} : ')
        lista_de_tarefas.append(novaTarefa)


    elif escolha == '2':
        print('\nSua Lista de Tarefas: ')
        sleep(1)
        for indice, elemento in enumerate(lista_de_tarefas):
            print(f'{indice+1}.[ ] {elemento}')

    elif escolha == '3':
        print('\nSua Lista de Tarefas:')
        for elemento in lista_de_tarefas:
            print(f'[ ] {elemento}')
        tarefa = input('\nQual tarefa você deseja atualizar? ')
        indice = lista_de_tarefas.index(tarefa)
        atualizacao_de_tarefa = input('\nQual a atualização da tarefa? ')
        lista_de_tarefas.insert(indice, atualizacao_de_tarefa)
        lista_de_tarefas.remove(tarefa)

    elif escolha == '4':
        for elemento in lista_de_tarefas:
            print(f'[ ] {elemento}')

        tarefa_completada = input('Qual a Tarefa foi Completada? ')
        lista_de_tarefas.remove(tarefa_completada)
        lista_de_tarefas_completadas.append(tarefa_completada)

        for elemento in lista_de_tarefas_completadas:
            print(f'[x] {elemento}')

    elif escolha == '5':
        for indice, elemento in enumerate(lista_de_tarefas_completadas):
            print(f'{indice+1}.[x] {elemento}')
            print('Deletando a Tarefa Completada...')
            sleep(1)
            lista_de_tarefas_completadas = []

    elif escolha == '6':
        print(f'\n{cor_texto_vermelho}Fechando Gerenciador de Tarefas...{fechamento}')
        sleep(1.5)
        break