distancia = float(input("Digite a distância percorrida (em km): "))

gasto = float(input("Digite a quantidade de combustível gasta (em litros): "))

consumo_medio = distancia / gasto
print("O consumo médio do automóvel é de", round(consumo_medio, 2), "km/l.")#round serve para aredondar em um determinado numero de casas

