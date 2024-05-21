alunos = ['viktor']
alunos.append('lucas')
while True:
    nome = input('Digite o nome do aluno: ')
    alunos.append(nome)
    resposta =input('Deseja adicionar mais um aluno? (s/n): ')
    if resposta.upper() == 'N':
        break
print("Alunos cadastradas: {alunos}")    