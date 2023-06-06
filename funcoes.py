def somatorio(dados,coluna):
    soma = 0
    for registro in dados:
        soma += registro[coluna]
    return soma 

def media(dados,coluna):
    soma = 0
    for registro in dados:
        soma += registro[coluna]
        
    return soma / len(dados)   