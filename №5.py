values = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]


def to_roman(number: int):
    """

    Переводит обычные цифры в римские

    Args:
        number (int): Исходное обычное число

    Returns:
        str: Римское число

    Raises:
        ValueError: Если введен текст неправильного формата

    Example:
        >> check_winners(3)
        III
    """
    result = ""
    for value, letter in values:
        while number >= value:
            result += letter
            number -= value
    return result


def from_roman(roman: str):
    """

    Переводит римские числа в обычные

    Args:
        roman (str): Исходное римское число

    Returns:
        int: Обычное число

    Raises:
        ValueError: Если введен текст неправильного формата

    Example:
        >> check_winners(III)
        3
    """
    digits = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(roman)):
        current = digits[roman[i]]
        # Если следующая цифра больше — текущую вычитаем (IV = 5 - 1)
        if i + 1 < len(roman) and digits[roman[i + 1]] > current:
            result -= current
        else:
            result += current
    return result

# Тест
roman_tests = ["IV", "IX", "XLII", "XCIX", "MMXXIII"]
for roman in roman_tests:
    number = from_roman(roman)
    print(roman, "->", number, "->", to_roman(number))