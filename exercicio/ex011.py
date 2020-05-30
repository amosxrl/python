print('Quantidade de tinta nescessario.')
lar = float(input('Largura da parede: '))
alt = float(input('Altura da Parede: '))
area = lar * alt
tinta = area / 2
print('Sua parede é de {:.2f}m²:'.format(area))
print('Precisa de aprocimadamente {:.3f}l de tinta.'.format(tinta))