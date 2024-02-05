def printInfoInput(ltc, rzm, qMalte, absMalte, evap, trubQ, trubF):
    i = f"""
{'__' * 40}

    Volume final esperado: | {ltc} litor
    Razão água/malte:      | {rzm}
    Quantidade de malte:   | {qMalte} Kg
    Absorção do malte:     | {absMalte} L/kg.
    Evaporação:            | {evap} litros.
    Trub quente:           | {trubQ} litros.
    Trub frio:             | {trubF} litros.
    """
    print(i)


def printInfo(ltc, agua_mostura, agua_lavagem, perdas, agua_total) -> None:

    i = f"""
{'__' * 40}

    Água de Mostura: | {agua_mostura} Litro
    Água de Lavagem: | {agua_lavagem} Litro
    Água de Perdas:  | {perdas} Litro

    Água de Total:   | {agua_total} Litro


    {'..' * 20}

    Água necessário para a produçao  de {ltc} litor cerveja é de {agua_total} litros

{'__' * 40}
    """
    print(i)
