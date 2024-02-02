


def printInfo(ltc,agua_mostura,agua_lavagem, perdas, agua_total) -> None:

    i = f"""

{'__' * 40}

    Volume final esperado: {ltc} litor

    Água de Mostura: | {agua_mostura} Litro
    Água de Lavagem: | {agua_lavagem} Litro
    Água de Perdas:  | {perdas} Litro

    Água de Total:   | {agua_total} Litro


    {'..' * 20}

    Água necessário para a produçao  de {ltc} litor cerveja é de {agua_total} litros

{'__' * 40}
    """
    print(i)
    