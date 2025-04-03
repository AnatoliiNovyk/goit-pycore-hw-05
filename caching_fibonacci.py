from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """
    Створює та повертає функцію fibonacci з кешуванням результатів.
    """
    cache = {}

    def fibonacci(n: int) -> int:
        """
        Обчислює n-те число Фібоначчі з використанням кешування.
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Приклад використання:
if __name__ == "__main__":
    fib = caching_fibonacci()
    print(fib(10))
    print(fib(15))
