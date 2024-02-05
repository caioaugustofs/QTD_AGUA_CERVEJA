from calc_aguaCerveja import CalculadoraAguaCerveja
from tools.printer import printInfo, printInfoInput
from tools.inputer import inputInfo


inf = inputInfo()


cev = CalculadoraAguaCerveja(**inf)
cev = cev.getinfo()

printInfoInput(**inf)


printInfo(
    ltc=inf['ltc'],
    agua_mostura=cev['agua_mostura'],
    agua_lavagem=cev['agua_lavagem'],
    perdas=cev['perdas'],
    agua_total=cev['agua_total'],
)
