def calcular_media(notas):
    soma=0
    for nota in notas:
        soma += nota
    media = soma / (len(notas) - 1)
    return media