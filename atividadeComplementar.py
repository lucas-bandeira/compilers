tokens = []

string = input("Digite um lexeme (uma tecla qualquer ou # para sair): ")
string_replaced = string.replace(" ", "")
string_size = len(string_replaced)

i = 0
count = 1
countOccurrences = 0

while i < string_size:
    lexeme = string_replaced[i]
    if lexeme == "+" or lexeme == "=" or lexeme == "*" or lexeme == "-":
        if countOccurrences == 0:
            if string_replaced[i - 1].isdigit():
                tokens.append("<%s>" % string_replaced[0:i])
                tokens.append("<%s>" % lexeme)
                i += 1
                countOccurrences = i
            else:
                tokens.append("<id, %s>" % count)
                tokens.append("<%s>" % lexeme)
                i += 1
                count += 1
                countOccurrences = i
        else:
            if string_replaced[i - 1].isdigit():
                tokens.append("<%s>" % string_replaced[countOccurrences:i])
                tokens.append("<%s>" % lexeme)
                i += 1
                countOccurrences = i
            else:
                tokens.append("<id, %s>" % count)
                tokens.append("<%s>" % lexeme)
                i += 1
                count += 1
                countOccurrences = i

    elif (i + 1) == string_size:
        if string_replaced[i - 1].isdigit():
            tokens.append("<%s>" % string_replaced[countOccurrences:i + 1])
            i += 1
            countOccurrences = i
        else:
            tokens.append("<id, %s>" % count)
            i += 1
            count += 1
            countOccurrences = i

    else:
        i += 1

print("tokens:", tokens)
