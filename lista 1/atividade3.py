quant_paes =int(input("digite a quantidade de paes vendidos"))
quant_broa =int(input("digite a quantidade de broas vendidos"))

arrecadado = (quant_paes * 0.12) + (quant_broa * 1.50)
popupança = (arrecadado * 0.10)

print("total de vendas de paes e broas foi: ",arrecadado)
print("quantidade de dinheiro que sera colocado na poupança sera: ",popupança)