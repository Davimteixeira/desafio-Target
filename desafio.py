# 1) Cálculo da variável SOMA
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print("O valor da variável SOMA é:", SOMA)
# O valor da variável SOMA ao final do processamento é 91.

# 2) Verificar se um número pertence à sequência de Fibonacci
def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

# Entrada do usuário
num = int(input("Digite um número: "))

if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")

# 3) Análise de faturamento diário
import json

with open('faturamento.json', 'r') as file:
    data = json.load(file)

faturamento_diario = data['faturamento_diario']
dias_validos = [valor for valor in faturamento_diario if valor > 0]
media_mensal = sum(dias_validos) / len(dias_validos) if dias_validos else 0

menor_faturamento = min(dias_validos) if dias_validos else 0
maior_faturamento = max(dias_validos) if dias_validos else 0
dias_acima_da_media = len([valor for valor in dias_validos if valor > media_mensal])

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")


# 4) Percentual de representação por estado
# Dados de faturamento por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_faturamento = sum(faturamento.values())

percentual = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento.items()}

for estado, pct in percentual.items():
    print(f"{estado}: {pct:.2f}%")


# 5) Inverter os caracteres de uma string
def inverter_string(s):
    resultado = ""
    for char in s:
        resultado = char + resultado
    return resultado

# Entrada do usuário
entrada = input("Digite uma string: ")
inversa = inverter_string(entrada)
print(f"String invertida: {inversa}")