total_dias = int(input("Digite o total de dias: "))

anos = total_dias // 365
resto = total_dias % 365

meses = resto // 30
dias = resto % 30

print(f"{anos} ano(s), {meses} mes(es), {dias} dia(s)")
