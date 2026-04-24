contador= 1
while contador <=3:
    nota = float(input(f"Digite a {contador} nota"))
    if nota < 0 or nota > 10:
       nota = float(input(f"Nota Invalida. Digite a {contador} nota Novamente")) 
    soma + nota + contador
    contador+= +1
    soma = nota

media = nota / (1+2+3)
print ("A media das notas é: ", media)