mao_de_obra = {
    "OFICIAL": 8.59,
    "MEIOS_OFICIAIS": 6.45,
    "AJUDANTE": 6.22,
    "OPERADOR": 9.52,  # Operador de máquina pesada
    "MOTORISTA": 9.55,  # Motorista basculante geral
    "VIGIA": 6.22,
    "ENGENHEIRO": 36.36,
}

mao_de_obra_digitada = str(input("Escolha a mão de obra desejada: "))
# valor_mao_de_obra = float(input('Insira o valor da mão de obra: '))
# encargos = float(input('insira o valor dos encargos sociais em números decimais: '))

valor_mao_de_obra = mao_de_obra.get(mao_de_obra_digitada, None)

if valor_mao_de_obra is None:
    print("Valor de mão de obra, não está cadastrado!")
    exit(1)

v1 = float(input("Insira o valor da mão de obra: "))
v2 = float(input("Insira o valor do encargo: "))
v3 = v1 / v2
if v3 >= valor_mao_de_obra:
    print(f"O valor da mão de obra é R${v3}. Acima da tabela do sindicato!")
else:
    print(f"O valor da mão de obra é R${v3}. Abaixo da tabela do sindicato!")
