operadores = []

s = input("Digite um lexema (uma tecla qualquer ou # para sair): ")
tamanho = len(s)

i = 0
count = 1

while i < tamanho:
    lexema = s[i]
    if lexema.isalpha():
        operadores.append("<id, %s>" % count)
        i += 1
        count += 1

    elif lexema.isdigit():
        # operadores.append("<num, %s>" % count)
        # count += 1
        operadores.append("<%s>" % lexema)
        i += 1

    elif lexema == "+" or lexema == "=" or lexema == "*":
        operadores.append("<%s>" % lexema)
        i += 1

    elif lexema == "#":
        print("Operadores:", operadores)
        break

    elif lexema == ' ':
        i += 1

    else:
        print("<erro>")

print("Operadores:", operadores)
