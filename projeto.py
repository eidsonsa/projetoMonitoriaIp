import matplotlib.pyplot as plt

class Carro:

    def __init__(self, nome, ano, km, cor, portas):
        self.nome = nome
        self.ano = ano
        self.km = km
        self.cor = cor
        self.portas = portas

carros = []

for i in range(1, 15):
    s = 'test' + str(i) + '.txt'
    carro = open(s, 'r', encoding='utf8')
    linhas = carro.readlines()
    
    nome = linhas[0] 
    ano = None
    km = None
    cor = None 
    portas = None
    
    for j in range(0, len(linhas) - 1):
        if linhas[j] == 'Modelo\n':
            nome = linhas[j + 1]
        if linhas[j] == 'Ano\n' or linhas[j] == 'ANO\n':
            ano = linhas[j + 1]
        if linhas[j] == 'KM\n' or linhas[j] == 'Quilometragem\n':
            km = linhas[j + 1]
        if linhas[j] == 'Cor\n' or linhas[j] == 'COR\n':
            cor = linhas[j + 1]
        if linhas[j] == 'Portas\n' or linhas[j] == 'PORTAS\n':
            portas = linhas[j + 1]
    
    if portas is None:
        portas = 'Nao especificado'

    portas.replace(' portas', '')
    carrobj = Carro(nome, ano, km, cor, portas)
    carros.append(carrobj)  

nomes = [i.nome.replace('\n', '') for i in carros if i.nome is not None]
anos = [i.ano.replace('\n', '') for i in carros if i.ano is not None]
kms = [i.km.replace('\n', '') for i in carros if i.km is not None]
cores = [i.cor.replace('\n', '') for i in carros if i.cor is not None]
portas = [i.portas.replace(' portas', '').replace('\n', '') for i in carros if i.portas is not None]

plt.plot(anos, nomes)
plt.title('Anos de lançamento')
plt.xlabel('Ano')
plt.ylabel('Carro')
plt.show()

plt.plot(kms, nomes)
plt.title('Kms rodados')
plt.xlabel('Km')
plt.ylabel('Carro')
plt.show()

plt.plot(cores, nomes)
plt.title('Cores')
plt.xlabel('Cor')
plt.ylabel('Carro')
plt.show()

plt.plot(portas, nomes)
plt.title('Quantidade de portas')
plt.xlabel('Quantidade de portas')
plt.ylabel('Carros')
plt.show()

