def validar_entrada(n):
    if not isinstance(n, int) or n <= 1:
        raise ValueError("O número deve ser um inteiro maior que 1.")

def primos_linear(n: int) -> list:
    validar_entrada(n)

    
    eh_primo = [True] * (n + 1)
    eh_primo[0], eh_primo[1] = False, False

    primos = []
    
    for i in range(2, n + 1):
        if eh_primo[i]:
            primos.append(i)
            for múltiplo in range(i * 2, n + 1, i):
                eh_primo[múltiplo] = False

    return primos

while True:
    try:
        n = int(input("Digite um número inteiro maior que 1: "))
        validar_entrada(n)
        print(f"Números primos até {n}: {primos_linear(n)}")
        break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro maior que 1.")
