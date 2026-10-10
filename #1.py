# Задание шифр Цезаря
def tozezhar(sent: str, shag: int):
    """
    Зашифровывает сообщение по шифру Цезаря с указаным шагом.

    Args:
        sent (str): Исходный текст
        shag (int): Шаг для зашифровки текста с помощью шифра Цезаря

    Returns:
        str: Итоговый зашифрованный текст

    Raises:
        ValueError: Если введен текст на каком-то языке кроме русского
                    и английского.

    Example:
        >> tozezhar(ABCD, 1)
        BCDE
    """
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    RUS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    leng = ''
    if sent[0] in ABC:
        leng = 'английский'
    elif sent[0] in RUS:
        leng = 'русский'
    print(leng)
    korkas = ''
    if leng == 'английский':
        korkas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif leng == 'русский':
        korkas = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    newsent = ''
    for i in range(len(sent)):
        if (korkas.find(sent[i]) + (shag)) <= (len(korkas) - 1):
            newsent += korkas[korkas.find(sent[i]) + (shag)]
        elif (korkas.find(sent[i]) + (shag)) > (len(korkas) - 1):
            newsent += korkas[(korkas.find(sent[i]) + (shag)) - (len(korkas))]
    return newsent
def outzezhar(sent: str, shag: int):
    """
    Расшифровывает сообщение по шифру Цезаря с указаным шагом.

    Args:
        sent (str): Исходный текст
        shag (int): Шаг для расшифровки текста с помощью шифра Цезаря

    Returns:
        str: Итоговый расшифрованный текст

    Raises:
        ValueError: Если введен текст на каком-то языке кроме русского
                    и английского.

    Example:
        >> outzezhar(BCDE, 1)
        ABCD
    """
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    RUS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    leng = ''
    if sent[0] in ABC:
        leng = 'английский'
    elif sent[0] in RUS:
        leng = 'русский'
    print(leng)
    korkas = ''
    if leng == 'английский':
        korkas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif leng == 'русский':
        korkas = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    newsent = ''
    for i in range(len(sent)):
        if (korkas.find(sent[i]) - (shag)) >= 0:
            newsent += korkas[korkas.find(sent[i]) - (shag)]
        elif (korkas.find(sent[i]) - (shag)) < 0:
            newsent += korkas[(korkas.find(sent[i]) - (shag)) + (len(korkas))]
    return newsent

print('Расшифровать / Зашифровать')
shto = input() # Выбор Расшифровать/Зашифровать
sent = input() # Исходный текст
shag = int(input()) # С каким шагом расшифровать/зашифровать
if shto == 'Расшифровать':
    print(outzezhar(sent, shag))
else:
    print(tozezhar(sent, shag))