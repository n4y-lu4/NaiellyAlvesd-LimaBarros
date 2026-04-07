salario_atual = float(input("Salário atual: "))
percentual = float(input("Percentagem de aumento (ex: 10 para 10%): "))

#  Calcula apenas o valor do aumento em dinheiro
valor_do_aumento = salario_atual * (percentual / 100)

# Soma o aumento ao salário que a pessoa já tinha
novo_salario = salario_atual + valor_do_aumento

print(f"O aumento é de: {valor_do_aumento:.2f}€")
print(f"O novo salário será: {novo_salario:.2f}€")

#chato de fazer