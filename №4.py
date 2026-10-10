# Генерация пароля с английскими буквами
import random

def parol(nnr: str, nvr: str, ss: str, zfr: str, leng: int):
    """
    Гнерирует пароль по заданным параметрам

    Args:
        nnr (str): Наличие нижнего регистра
        nvr (str): Наличие верхнего регистра
        ss (str): Наличие специальных символов
        zfr (str): Наличие цифр
        leng (int): Длина пароля

    Returns:
        str: Итоговый пароль

    Raises:
        ValueError: Если введен текст неправильного формата
    """
    vreg = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    nreg = 'qwertyuiopasdfghjklzxcvbnm'
    z = '1234567890'
    s = '!@#$%^&*'

    groups = []
    if nnr == 'да': groups.append(nreg)
    if nvr == 'да': groups.append(vreg)
    if zfr == 'да': groups.append(z)
    if ss == 'да': groups.append(s)

    if not groups:
        print("Нужно выбрать хотя бы один тип символов")
    else:
        password = [random.choice(g) for g in groups]  # По одному из каждой группы
        chars = "".join(groups)
        while len(password) < leng:  # Добираем до нужной длины
            password.append(random.choice(chars))
        random.shuffle(password)
        print("Ваш пароль:", "".join(password))


print('Нужен ли нижний регистр: (да/нет)')
i1 = input()
print('Нужен ли верхний регистр: (да/нет)')
i2 = input()
print('Нужны ли специальные символы: (да/нет)')
i3 = input()
print('Нужны ли цифры: (да/нет)')
i4 = input()
print('Длина пароля:')
leng = int(input())
parol(i1, i2, i3, i4, leng)

