import matplotlib.pyplot as plt

class Carro:

    def __init__(self, nome, ano, km, cor, portas):
        this.nome = nome
        this.ano = ano
        this.km = km
        this.cor = cor
        this.portas = portas

carros = []

for i in range(1, 15):
    s = 'test' + str(i) + '.txt'
    carro = open(s, 'r')
    cabeçalho = carro.readline()
    # for j, linha in enumerate(carro):
    nome, cidade, cabAno, ano, cabKm, km, cabCor, cor,  cabPortas, portas, preco, specs = carro.split('\n')
    carrobj = Carro(nome, ano, km, cor, portas)
    carros.append(carrobj)  