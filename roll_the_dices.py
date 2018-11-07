import random

def roll_the_dice(minimo = 1, maximo = 6):
    return int(random.uniform(minimo, maximo + 1))


print('---- Role os dados ----')
print('Escolha que dado deseja rolar digitando o valor mínimo e máximo')
print('Ou role o famoso d6 apertando \'Enter\' duas vezes')
print('Boa sorte!')
print('-----------------------')
print()

continua = True
while continua :
    minimo = input('Digite o valor mínimo: ')
    maximo = input('Digite o valor máximo: ')

    try:
        minimo = int(minimo)
    except:
        minimo = 1

    try:
        maximo = int(maximo)
    except:
        maximo = 6

    res = roll_the_dice(minimo, maximo)
    print()
    print(f'O valor do dado foi: {res}')
    print()

    usuario_quer_continuar = input('Deseja rolar o dado novamente? [S/N]')

    continua = False
    if(usuario_quer_continuar == 'S' or usuario_quer_continuar == 's'):
        continua = True

print()
print('Programa encerrado!')