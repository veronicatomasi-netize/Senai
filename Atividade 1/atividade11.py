contador = 1
soma = 0
while contador <= 5:
    salario = float(input(f"digite o salario do {contador} Funcionario:  "))
    contador += 1
    soma += salario
media = soma / 5
print ("A medida dos salarios dos 5 funcionarios é: ", media)