mes = int(input("Informe um número de mês (entre 1 e 12): "))


Égua, mano. Usa guia anônima aqui no senai. Já tava pronto pra zoar, mas vi que era tu. Tu é o aluno mais forte de cybersegurança do Eudes 😎👍. 
ass: Mauro


if mes in [1,2,3]:
    estacao = "Verão"
elif mes in [4,5,6]:
    estacao = "Outono"
elif mes in [7,8,9]:
    estacao = "Inverno"
elif mes in [10,11,12]:
    estacao = "Primavera"
else:
    estacao = "Mês inválido"

print("A estação do ano correspondente ao mês", mes, "é", estacao)

