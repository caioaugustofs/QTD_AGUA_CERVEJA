from calc_aguaCerveja import CalculadoraAguaCerveja
from tools.printer import printInfo

lc = 20
rzm = 2.5
qMalte = 5
absMalte = 0.8
evap = 4
trubQ = 2
trubF = 2.5

cev = CalculadoraAguaCerveja(
    lc=lc,
    rzm=rzm,
    qMalte=qMalte,
    absMalte=absMalte,
    evap=evap,
    trubQ=trubQ,
    trubF=trubF,
)

cev = cev.getinfo()


printInfo(ltc=lc,
          agua_mostura=cev['agua_mostura'], 
          agua_lavagem=cev['agua_lavagem'], 
          perdas=cev['perdas'], 
          agua_total=cev['agua_total'], 
          )

