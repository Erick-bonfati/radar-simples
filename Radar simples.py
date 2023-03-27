#Eu quero multar os carros baseados na sua velocidade atual, faça um programa em que 
#Faça descobrir se o usuario, estava acima da velocidade, abaixo, ou na velocidade indicada
#Pela rodovia, e com base nisso, de a multa adequada!


print('O limite do radar é de 80Kmh')

vel_carro = int(input('Digite em que velocidade o carro estava: '))

aviso = 'Sem multas, porem 4 pontos na carteira serão perdidos!'
multa_leve = 'R$150,00 e 4 pontos na carteira!'
multa_normal = 'R$250,00 e 6 pontos na carteira!'
multa_grave = 'R$400,00 e 8 pontos na carteira!'
multa_gravissima = 'R$800,00 e perda de carteira!'


if vel_carro <= 80:
    print('Carro dentro do limite de velocidade, não houve multas')
elif vel_carro <= 85:
    print(f'Carta de aviso: {aviso}')
elif vel_carro <= 100:
    print(f'Acima da velocidade, sua multa é de {multa_leve}')
elif vel_carro <= 120:
    print(f'Pouco acima da velocidade, sua multa é de {multa_normal}')
elif vel_carro <= 150:
    print(f'Muito acima da velocidade, sua multa é de {multa_grave}')
else:
    print(f'Velocidade gravissima, sua multa é de {multa_gravissima}')

