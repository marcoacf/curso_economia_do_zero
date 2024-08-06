# MÓDULO 1: PYTHON DO ZERO



### Aula 1 - Aprendizados:
#### Tratando dados reais do zero (fundos de investimento)
 - Usando Pandas pela primeira vez
 - Como importar dados do Excel
 - Como excluir e criar colunas em tabelas
 - Como filtrar dataframes e criar variáveis
 - Cálculos entre diferentes colunas
 - Primeiro gráfico em Python

 ### Aula 2 - Aprendizados:
 #### Tipos de dados, nomenclaturas e funções básicas
 - Listas, dicionários
 - String, float, integer
 - Date e datetime

 ### Aula 3 - Aprendizados:
 #### Alterando tipos de dados
 - Método .info()
 - index > datetime
 - float > string(object) astype
 - string > float astype
 - datetime > string astype
 - string > datetime (64ns)

 ### Aula 4 - Aprendizados:
 #### Ordenando os dados e operações matemáticas
 - Método .sort()
 - Métodos .sort_values() e .sort_index()
 - Operadores básicos
 - Módulo "math"

 ### Aula 5 - Aprendizados:
 #### Localização cirúrgica dos dados
 - Métodos .loc e .iloc
 - Método de ajuda (help)
 
 ### Aula 6 - Aprendizados:
 #### Funções de texto
 - Concatenação
 - Limpeza de espaços
 - F-String
 - Conversão
 
 ### Aula 7 - Aprendizados:
 #### Formatando tabelas e dados financeiros no padrão brasileiro
 - 

 ```

!pip install Jinja2

!pip install tabulate

import pandas as pd

tabela = pd.DataFrame(
    {

        "strings":["abcd","bcde","cdef"],
        "ints":[1,2,3],
        "floats":[1.234, 1000.23, 1500500.8501]
    }
)

tabela

```

|    | strings   |   ints |        floats |
|---:|:----------|-------:|--------------:|
|  0 | abcd      |      1 |    1.234      |
|  1 | bcde      |      2 | 1000.23       |
|  2 | cdef      |      3 |    1.5005e+06 |


```

tabela.style.format(precision=2, thousands=".", decimal=",")

```

|    | strings   |   ints |        floats |
|---:|:----------|-------:|--------------:|
|  0 | abcd      |      1 |          1,23 |
|  1 | bcde      |      2 |      1.000,23 |
|  2 | cdef      |      3 |  1.500.500,85 |


