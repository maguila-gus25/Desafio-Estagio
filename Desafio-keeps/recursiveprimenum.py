def validar_entrada(n):
    if not isinstance(n, int) or n <= 1:
        raise ValueError("O número deve ser um inteiro maior que 1.")

def eh_primo(n, divisor=2):
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return eh_primo(n, divisor + 1)

def primos_recursivo(n, atual=2, lista=None):
    if lista is None:
        lista = []
    
    if atual > n:
        return lista

    if eh_primo(atual):
        lista.append(atual)

    return primos_recursivo(n, atual + 1, lista)

try:
    n = int(input("Digite um número inteiro maior que 1: "))
    validar_entrada(n)
    print(f"Números primos até {n}: {primos_recursivo(n)}")
except ValueError:
    print("Entrada inválida. Digite um número inteiro maior que 1.")
