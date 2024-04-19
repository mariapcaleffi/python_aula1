produtos = ["arroz", "feijão", "milho", "trigo", "soja"]
precos = [5.4, 6.8, 3.2, 4.28, 3.99]
quantidades = [5000, 6000, 7000, 4500, 2800]
totais = []
for i in range(5):
    totais.append(precos[i] * quantidades[i])
print(totais)