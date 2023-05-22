dinheiro = float(input("Digite o valor em dólar ou euro que deseja converter para reais: "))

moeda = input("Digite a tecla 'd' para dólar ou 'e' para Euro: ")

if moeda == 'd':
    transformacao = 5.01

elif moeda == 'e':
    transformacao = 5.49

else:
    print("Essa moeda não condiz com as que foram declaradas acima.")
    exit(0)

resultado = dinheiro * transformacao
print(f"O valor de {dinheiro:.2f} {moeda.upper()} em reais é de {resultado:.2f} reais.")

