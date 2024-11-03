import random

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('terceiro aluno: ')
aluno4 = input('Quarto Aluno: ')

lista = [aluno1,aluno2,aluno3,aluno4]
sorteio = random.choice(lista)

print('O aluno sorteado foi: {}'.format(sorteio))