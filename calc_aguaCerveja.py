class CalculadoraAguaCerveja:
    """Calculadora de água para produção de cerveja.

    Calcula a quantidade de água necessária para produção de cerveja,
    considerando perdas por evaporação, trub, absorção do malte e contração
    pela temperatura.

    Args:
        ltc (float): Litros de cerveja final em Litro.
        rzm (float): Razão água/malte.
        qMalte (float): Quantidade de malte em Kg.
        absMalte (float): Absorção do malte em L/kg.
        evap (float): Evaporação em litros.
        trubQ (float): Trub quente em litros.
        trubF (float): Trub frio em litros.

    Returns:
        dict: Dicionário com os seguintes valores:
            * agua_mostura: Quantidade de água de mostura em litros.
            * agua_lavagem: Quantidade de água de lavagem em litros.
            * perdas: Perdas totais em litros.
            * agua_total: Quantidade total de água em litros.
    """

    def __init__(
        self,
        ltc: float,
        rzm: float,
        qMalte: float,
        absMalte: float,
        evap: float,
        trubQ: float,
        trubF: float,
    ) -> None:

        self.ltc = ltc  # Litros de cerveja Final esperados em Litro
        self.rzm = rzm  # Razão Água Malte
        self.qMalte = qMalte  # Quantidade De Malte_Kg
        self.absMalte = absMalte  # Absorcao do malte L/kg
        self.evap = evap  # Evaporação litros
        self.trubQ = trubQ  # Trub quente litros
        self.trubF = trubF  # Trub frio litros
        self.crontTemp = 0.04  # Contração pela temperatura

    def perdasTrubTotal(self) -> float:
        """Calcula as perdas totais por trub."""
        return self.trubQ + self.trubF

    def perdasContracao(self) -> float:
        """Calcula as perdas por contração pela temperatura."""
        return (self.ltc + self.evap + self.perdasTrubTotal()) * self.crontTemp

    def perdasMalte(self):
        """Calcula as perdas por absorção do malte."""
        return self.absMalte * self.qMalte

    def perdas(self) -> float:
        """
        Calcula as perdas totais do sistema.

        Retorna:
            float: Perdas totais em litros.
        """

        return (
            self.perdasMalte()
            + self.evap
            + self.perdasTrubTotal()
            + self.perdasContracao()
        )

    def aguaMostura(self) -> float:
        """
        Calcula a quantidade de água de mostura.

        Retorna:
            float: Água de mostura em litros.
        """
        return self.rzm * self.qMalte

    def aguaLavagem(self) -> float:
        """
        Calcula a quantidade de água de lavagem.

        Retorna:
            float: Água de lavagem em litros.
        """

        return self.ltc - self.aguaMostura() + self.perdas()

    def aguaTotal(self) -> float:
        """
        Calcula a quantidade total de água necessário para produzir x litros de cerveja.

        Retorna:
            float: Água total em litros.
        """
        return self.aguaMostura() + self.aguaLavagem()

    def getinfo(self) -> dict:
        """Retorna um dicionário com as informações da calculadora."""
        return {
            'agua_mostura': self.aguaMostura(),
            'agua_lavagem': self.aguaLavagem(),
            'perdas': self.perdas(),
            'agua_total': self.aguaTotal(),
        }
