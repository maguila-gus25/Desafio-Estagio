def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

while True:
    try:
        n = int(input("Insira um número inteiro: "))
        if n < 0:
            raise ValueError("O número deve ser maior ou igual a zero.")
        print(f"Resultado: {fib(n)}")
        break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro maior ou igual a zero.")