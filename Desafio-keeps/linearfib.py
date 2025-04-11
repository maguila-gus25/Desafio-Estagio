def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

while True:
    try:
        n = int(input("Insira um número inteiro: "))
        if n < 0:
            raise ValueError("O número deve ser maior ou igual a zero.")
        print(f"Resultado: {fib(n)}")
        break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro maior ou igual a zero.")