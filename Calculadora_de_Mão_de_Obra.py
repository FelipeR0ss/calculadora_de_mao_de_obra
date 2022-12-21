mao_de_obra = {
   "PEDREIRO": 8.59,
    "CARPINTEIRO": 8.59,
    "ARMADOR": 8.59,
    "SOLDADOR": 8.59,
    "ELETRICISTA": 8.59,
    "ENCANADOR": 8.59,
    "VIDRACEIRO": 8.59,
    "MONTADOR": 8.59,
    "TOPOGRAFO": 8.59,
    "ASSENTADOR": 8.59, # Assentador de tubos
    "NIVELADOR": 8.59,
    "DESENHISTA": 8.59,
    "ALMOXARIFE": 8.59,
    "JARDINEIRO": 8.59,
    "PINTOR": 8.59,
    "SERRALHEIRO": 8.59,
    "AJUDANTES": 6.45, # Ajudante Especializado
    "OPERADORB": 6.45, # Operador de Betoneira
    "SERVENTEH": 6.45, # Servente Habilitado
    "AJUDANTE": 6.22,
    "SERVENTE": 6.22,
    "OPERADOR1": 9.52,  # Operador de Pá Carregadeira
    "OPERADOR2": 9.52,  # Operador de Trator de Esteira ou Lâmina
    "OPERADOR3": 9.52,  # Operador de Retroescavadeira
    "OPERADOR4": 9.52,  # Operador Geral
    "MOTORISTA1": 9.55,  # Motorista Basculante
    "MOTORISTA2": 9.55,  # Motorista Geral
    "ENCARREGADO": 10.0, # Encarregado Geral
    "MESTRE": 10.0, # Mestre de Obras
    "VIGIA": 6.22, # Vigia Noturno
    "ENGENHEIRO": 36.36,
}

mao_de_obra_digitada = str(input("Escolha a mão de obra desejada: "))

valor_mao_de_obra = mao_de_obra.get(mao_de_obra_digitada, None)

if valor_mao_de_obra is None:
    print("Valor de mão de obra, não está cadastrado!")
    exit(1)

v1 = float(input("Insira o valor da mão de obra: "))
v2 = float(input("Insira o valor do encargo: "))
v3 = v1 / v2
if v3 >= valor_mao_de_obra:
    print(f"O valor da hora trabalha para {mao_de_obra_digitada} é R${v3:.2f}. Acima da tabela do sindicato!")
else:
    print(f"O valor da hora trabalha para {mao_de_obra_digitada} é R${v3:.2f}. Abaixo da tabela do sindicato!")
