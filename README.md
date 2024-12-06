# QTD_AGUA_CERVEJA

## Calcular a quantidade de água necessária para produzir X litros de cerveja

Este projeto calcula a quantidade de água necessária para produção de cerveja, considerando perdas por evaporação, trub, absorção do malte e contração pela temperatura.

## Pré-requisitos

- Python 3.x
- pip

## Instalação

1. Clone o repositório:

2. Navegue até o diretório do projeto

```sh
cd QTD_AGUA_CERVEJA
```

3. Instale as dependências necessárias
```sh
pip install -r requirements.txt
```
### Uso
```sh
from calc_aguaCerveja import CalculadoraAguaCerveja

resultado = CalculadoraAguaCerveja(
        ltc=20.0,
        rzm=3.0,
        qMalte=5.0,
        absMalte=1.0,
        evap=4.0,
        trubQ=1.0,
        trubF=1.0
    )

print(f"Quantidade de água necessária: {resultado} litros")
