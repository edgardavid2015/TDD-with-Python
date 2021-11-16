import re


def suma(operands):
    if operands == '':
        return 0
    resultado = 0
    for item in re.split(r'[,\n]', operands):
        if item == '':
            raise ValueError
        resultado += int(item)

    return resultado
