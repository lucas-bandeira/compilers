from tabulate import tabulate

tokens = []

special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                      '>', '?', '@', '[', ']', '^', '_', '`,' '{', '|', '}', '~']

string = input("Digite um lexeme (uma tecla qualquer ou # para sair): ")
string_replaced = string.replace(" ", "")
string_size = len(string_replaced)

table = [['ID', ' ']]

i = 0
count = 1
countOccurrences = 0

while i < string_size:
    lexeme = string_replaced[i]

    if lexeme in special_characters:
        if countOccurrences == 0:
            if string_replaced[i - 1].isdigit():
                tokens.append("<%s>" % string_replaced[0:i])
                tokens.append("<%s>" % lexeme)
                i += 1
                countOccurrences = i
            else:
                if string_replaced[0:i] in table:
                    print('esta na lista')
                # table.append('{0}   {1}'.format(count, string_replaced[0:i]))
                table.append(['{0}'.format(count), '{0}'.format(string_replaced[0:i])])
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
                if string_replaced[countOccurrences:i] in table:
                    print('esta na lista')
                # table.append('{0}   {1}'.format(count, string_replaced[countOccurrences:i]))
                table.append(['{0}'.format(count), '{0}'.format(string_replaced[countOccurrences:i])])
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
            if string_replaced[countOccurrences:i + 1] in table:
                print('esta na lista')
            # table.append('{0}   {1}'.format(count, string_replaced[countOccurrences:i + 1]))
            table.append(['{0}'.format(count), '{0}'.format(string_replaced[countOccurrences:i + 1])])
            tokens.append("<id, %s>" % count)
            i += 1
            count += 1
            countOccurrences = i

    else:
        i += 1

print("table:", tabulate(table))
# print("list:", table)
print("tokens:", tokens)
