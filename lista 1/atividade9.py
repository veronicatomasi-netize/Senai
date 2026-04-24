preco_pequeno =10
preco_medias =12
preco_grande =15

quantidade_pequenas = int(input("digite a quantidade de xamisetas pequenas: "))
quantidade_medias = int(input("digite a quantidade de xamisetas medias: "))
quantidade_grandes = int(input("digite a quantidade de xamisetas grandes: "))

valor_arrecadado = (quantidade_pequenas + preco_pequeno) + (quantidade_medias + preco_medias) + (quantidade_grandes + preco_grande)

print("o valor total arrecadado é : ", valor_arrecadado)