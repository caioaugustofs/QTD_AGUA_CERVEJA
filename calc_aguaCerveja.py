class Calculadora_AguaCerveja:
    """Calcula a quantidade de água necessária para produção de cerveja.

    Args:
        lc (float): Litros de cerveja final em Litro.
        rzm (float): Razão água/malte.
        qMalte (float): Quantidade de malte em Kg.
        absMalte (float): Absorção do malte em L/kg.
        evap (float): Evaporação em litros.
        trubQ (float): Trub quente em litros.
        trubF (float): Trub frio em litros.
    """

    def __init__(
        self,
        lc: float,
        rzm: float,
        qMalte: float,
        absMalte: float,
        evap: float,
        trubQ: float,
        trubF: float,
    ) -> None:
        
        self.lc = lc    # Litros de cerveja Final em Litro
        self.rzm = rzm  # razao Agua Malte
        self.qMalte = qMalte    # Quantidade De Malte_Kg
        self.absMalte = absMalte   # Absorcao do malte L/kg
        self.evap = evap  # evaporacao litros
        self.trubQ = trubQ   # trub quente litros
        self.trubF = trubF   # trub frio litros
        self.crontTemp = 0.04

    def perdas(self) -> float:
        """
        Calcula as perdas do sistema.

        Retorna:
            float: Perdas totais em litros.
        """
        abs_lavagem = self.absMalte * self.qMalte   # absorcao agua de lavagem

        contracao = (
            self.lc + self.evap + self.trubQ + self.trubF
        ) * self.crontTemp

        return abs_lavagem + self.evap + self.trubQ + self.trubF + contracao

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

        return self.lc - self.aguaMostura() + self.perdas()

    def aguaTotal(self) -> float:
        """
        Calcula a quantidade total de água.

        Retorna:
            float: Água total em litros.
        """
        return self.aguaMostura() + self.aguaLavagem()

    def getinfo(self) -> list[float]:
        return [
            self.aguaMostura(),
            self.aguaLavagem(),
            self.perdas(),
            self.aguaTotal(),
        ]
