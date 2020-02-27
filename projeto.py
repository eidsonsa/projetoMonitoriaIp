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

# tem q testar essa parada e eu acho q tem algo errado entao esperar

nomes = [i.nome for i in carros]
anos = [i.ano for i in carros]
kms = [i.km for i in carros]
cores = [i.cor for i in carros]
portas = [i.portas for i in carros]

plt.plot(anos, nomes)
plt.title('Anos de lançamento dos carros')
plt.xlabel('Anos de lançamento')
plt.ylabel('Carros')
plt.show()

plt.plot(kms, nomes)
plt.title('Kms rodados dos carros')
plt.xlabel('Kms rodados')
plt.ylabel('Carros')
plt.show()

plt.plot(cores, nomes)
plt.title('Cores dos carros')
plt.xlabel('Cores')
plt.ylabel('Carros')
plt.show()

plt.plot(portas, nomes)
plt.title('Quantidade de portas dos carros')
plt.xlabel('Quantidade de portas')
plt.ylabel('Carros')
plt.show()

