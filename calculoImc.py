peso = float(input("Digite o seu peso em kg: "))

altura = float(input("Digite a sua altura em metros: "))

imc = peso / altura **2

if imc < 18.5:
    diagnostico = "Peso abaixo do esperado "
elif imc < 25:
    diagnostico = "O peso esta normal"
elif imc < 30:
    diagnostico = "Sobrepeso"
elif imc < 35:
    diagnostico = "Obesidade classe I"
elif imc < 40:
    diagnostico = "Obesidade classe II"
else:
    diagnostico = "Obesidade classe III"

print("Seu IMC é de:", imc)

print("Diagnóstico:", diagnostico)

