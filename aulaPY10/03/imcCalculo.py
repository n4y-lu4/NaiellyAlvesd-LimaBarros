#10/3/26
#imc 
nome =input("nome:")
peso = float(input("peso:"))
altura = float(input("altura:"))

imc= peso / (altura **2)
print(f"imc de {nome}: {imc:.2f}" )

baixoPeso = imc <18.5
normal = (imc >= 18.5) and (imc <25)
sobrePeso = (imc>=30)

print("baixo peso ?",baixoPeso)
print("normal?",normal)
print("obesidade?",sobrePeso)