from time import sleep

lista_de_tarefas = []

while True:
    print('Menu do Gerenciador de Tarefas:')
    print('''
    1. Adicionar Tarefa
    2. Ver Tarefas
    3. Atualizar Tarefas
    4. Completar Tarefa
    5. Deletar Tarefas Completadas
    6. Sair''')
    escolha = int(input(('Digite sua Escolha: ')))
    if escolha == 1:
        novaTarefa = input('Adicione a tarefa: ')
        lista_de_tarefas.append(novaTarefa)
    elif escolha == 2: 
        print(lista_de_tarefas)
    elif escolha == 3:
        print(lista_de_tarefas)
        tarefa = input('Qual tarefa você deseja atualizar? ')
        indice = lista_de_tarefas.index(tarefa)
        atualizacao_de_tarefa = input('Qual a atualização da tarefa? ')
        lista_de_tarefas.insert(indice, atualizacao_de_tarefa)
        lista_de_tarefas.remove(tarefa)
    elif escolha == 4:
        print(lista_de_tarefas)
        lista_de_tarefas_completadas = []
        tarefa_completada = input('Qual a Tarefa foi Completada? ')
        lista_de_tarefas.remove(tarefa_completada)
        lista_de_tarefas_completadas.append(tarefa_completada)
        print(lista_de_tarefas_completadas)
    elif escolha == 5:
        lista_de_tarefas_completadas = []
        print(lista_de_tarefas_completadas)
    elif escolha == 6:
        print('Fechando Gerenciador de Tarefas...')
        sleep(1.5)
        break