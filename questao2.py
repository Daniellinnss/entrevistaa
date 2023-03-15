def calcular_pontuacao(dado1, dado2, dado3, dado4, dado5, dado6):
    # cria uma lista com os dados lançados
    dados = [dado1, dado2, dado3, dado4, dado5, dado6]
    
    # verifica se há um único número 1 ou 5 nos dados
    if dados.count(1) == 1:
        return 100
    elif dados.count(5) == 1:
        return 50
    
    # verifica se há três números iguais nos dados
    for i in range(1, 7):
        if dados.count(i) >= 3:
            if i == 1:
                return 1000
            else:
                return i * 100
    
    # verifica se há quatro números iguais nos dados
    for i in range(1, 7):
        if dados.count(i) == 4:
            return i * 200
    
    # verifica se há cinco números iguais nos dados
    for i in range(1, 7):
        if dados.count(i) == 5:
            return i * 400
    
    # verifica se há seis números iguais nos dados
    for i in range(1, 7):
        if dados.count(i) == 6:
            return i * 800
    
    # verifica se há três pares de números iguais nos dados
    if set(dados) == {dados[0], dados[1], dados[2], dados[3], dados[4], dados[5]}:
        return 800
    
    # verifica se há uma sequência de 1 a 6 nos dados
    if set(dados) == {1, 2, 3, 4, 5, 6}:
        return 1200
    
    # se não houver nenhuma das regras anteriores, retorna 0
    return 0
