km = float(input('Quantos Km foram percorridos com o carro? '))
dias = int(input('Por quantos dias o carro ficou alugado? '))
print('O preço total a pagar é de R${:.2f}'.format(60 * dias + 0.15 * km))
