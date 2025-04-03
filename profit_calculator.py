import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[str, None, None]:
    """
    Знаходить всі дійсні числа у тексті та повертає їх як генератор.
    """
    pattern = r"(?<!\S)\d+\.?\d*(?!\S)"
    for match in re.finditer(pattern, text):
        yield match.group(0)

def sum_profit(text: str, func: Callable[[str], Generator[str, None, None]]) -> float:
    """
    Використовує генератор для обчислення загальної суми чисел у рядку.
    """
    total_profit = 0
    for number_str in func(text):
        try:
            total_profit += float(number_str)
        except ValueError:
            # Обробка випадку, якщо знайдений рядок не вдається перетворити на число
            pass
    return total_profit

# Приклад використання:
if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
