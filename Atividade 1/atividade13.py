import time

tempo_resfriamento = 10

print("Iniciando processo de resfriamento...")
print(f"Tempo restante: {tempo_resfriamento} segundos")

while tempo_resfriamento > 0:
    time.sleep(1)
    tempo_resfriamento -= 1
    print(f"Tempo restante: {tempo_resfriamento} segundos")

print("Resfriamento concluído! A prensa pode ser aberta.")