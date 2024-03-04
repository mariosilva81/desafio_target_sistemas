# RESPOSTA 1:

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)


# ================================

# RESPOSTA 2:

# Obtém o número informado pelo usuário.
number = int(
    input("Digite um número para verificar se ele pertence à sequência de Fibonacci: ")
)


# Cria a sequência de Fibonacci até o número informado pelo usuário.
def fibonacci(number):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < number:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


fibonacci_sequence = fibonacci(number)


# Verifica se o número informado pertence à sequência de Fibonacci.
def fibonacci_verify(number, sequence):
    if number in sequence:
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} não pertence à sequência de Fibonacci.")


fibonacci_verify(number, fibonacci_sequence)


# ================================


# RESPOSTA 3:

# Vide arquivo README.md


# ================================


# RESPOSTA 4:

# Vide arquivo README.md


# ================================
