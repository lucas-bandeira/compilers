operadores = []

string = input("Digite um lexeme (uma tecla qualquer ou # para sair): ")
s = string.replace(" ", "")
tamanho = len(s)

i = 0
count = 1
countOcurrencies = 0

while i < tamanho:
    lexeme = s[i]
    if lexeme == "+" or lexeme == "=" or lexeme == "*" or lexeme == "-":
        if countOcurrencies == 0:
            if s[i-1].isdigit():
                operadores.append("<%s>" % s[0:i])
                operadores.append("<%s>" % lexeme)
                i += 1
                countOcurrencies = i
            else:
                operadores.append("<id, %s>" % count)
                operadores.append("<%s>" % lexeme)
                i += 1
                count += 1
                countOcurrencies = i
        else:
            if s[i-1].isdigit():
                operadores.append("<%s>" % s[countOcurrencies:i])
                operadores.append("<%s>" % lexeme)
                i += 1
                countOcurrencies = i
            else:
                operadores.append("<id, %s>" % count)
                operadores.append("<%s>" % lexeme)
                i += 1
                count += 1
                countOcurrencies = i

    elif (i + 1) == tamanho:
        if s[i-1].isdigit():
            operadores.append("<%s>" % s[countOcurrencies:i+1])
            i += 1
            countOcurrencies = i
        else:
            operadores.append("<id, %s>" % count)
            i += 1
            count += 1
            countOcurrencies = i

    else:
        i += 1


print("Operadores:", operadores)
