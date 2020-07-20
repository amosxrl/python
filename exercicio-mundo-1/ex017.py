from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
''' hp = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa mede: {:.2f}'.format(hp)) '''
hp = hypot(co, ca)
print('A hipotenusa mede: {:.2f}'.format(hp))
