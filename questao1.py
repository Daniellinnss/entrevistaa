def quebra_texto(texto, colunas):
    palavras = texto.split()
    linhas = []
    linha_atual = ""
    for palavra in palavras:
        if len(linha_atual) + len(palavra) + 1 <= colunas:
            if linha_atual:
                linha_atual += " "
            linha_atual += palavra
        else:
            linhas.append(linha_atual)
            linha_atual = palavra
    if linha_atual:
        linhas.append(linha_atual)
    return "\n".join(linhas)

texto = "Governo proíbe uso de animais em testes para cosméticos e perfumes"
colunas = 20
resultado = quebra_texto(texto, colunas)
print(resultado)
