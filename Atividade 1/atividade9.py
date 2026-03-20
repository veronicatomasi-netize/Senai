nome = input("insira seu nome")
idade = int(input("insira sua idade"))
while True:
    if idade > 120 or idade < 0:
        print("idade invalida: por favor, digite um valor menor ou igual a 120.")
        idade = int(input("insira sua idade"))
    else:
        break
dias_de_vida = idade * 365 
print(" seu total de dias é: ", dias_de_vida)