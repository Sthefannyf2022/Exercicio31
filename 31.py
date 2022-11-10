viagem = int(input('Qual a distância da viagem?'))
if viagem <= 200:
   print('O preço da passagem é {}'.format(viagem*0.50))
else:
   print('O preço da passagem é {}'.format(viagem*0.45))

