dist = int(input('Qual a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(dist))

if dist > 200:
    print('E o preço da sua passagem será de: R${}reais'.format(dist * 0.45))

else:
    print('E o preço da sua passagem será de:R${:.1f}reais'.format(dist * 0.50))

