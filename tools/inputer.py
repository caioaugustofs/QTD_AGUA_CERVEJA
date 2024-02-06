def inputInfo():

    ltc = float(input('Litros de cerveja final esperado: '))
    rzm = float(input('Razão água malte: '))
    qMalte = float(input('Quantidade de malte em Kg: '))
    absMalte = float(input('Absorção do malte em L/kg: '))
    evap = float(input('Evaporação em litros: '))
    trubQ = float(input('Trub quente em litro: '))
    trubF = float(input('Trub frio em litros: '))

    return {
        'ltc': ltc,
        'rzm': rzm,
        'qMalte': qMalte,
        'absMalte': absMalte,
        'evap': evap,
        'trubQ': trubQ,
        'trubF': trubF,
    }
