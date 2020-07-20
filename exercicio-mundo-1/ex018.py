import math
ang = float(input('Digite o Ângulo: '))
seno = math.sin(math.radians(ang))
cose = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O ângulo é {:.2f}, o seno {:.2f}, o cosseno {:.2f} e a tangente {:.2f}.'.format(ang, seno, cose, tang))
