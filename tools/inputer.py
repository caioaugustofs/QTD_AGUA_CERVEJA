def _validar_float(prompt: str) -> float:

    while True:
        valor = input(prompt)
        try:
            if valor != '':
                if float(valor) > 0:
                    return float(valor)

            print('Valor inválido')
        except ValueError:
            print('Valor inválido. Digite um número decimal.')


def inputInfo() -> dict:

    info: dict = {}

    info['ltc'] = _validar_float('Litros de cerveja final esperado: ')
    info['rzm'] = _validar_float('Razão água malte: ')
    info['qMalte'] = _validar_float('Quantidade de malte em Kg: ')
    info['absMalte'] = _validar_float('Absorção do malte em L/kg: ')
    info['evap'] = _validar_float('Evaporação em litros: ')
    info['trubQ'] = _validar_float('Trub quente em litro: ')
    info['trubF'] = _validar_float('Trub frio em litros: ')

    return info
