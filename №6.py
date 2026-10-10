def visiliza(slovo: str, oshibki: int):
    """
    Игра 'Виселица' (моя любимая)

    Args:
        slovo (str): Загаданное слово
        oshibki (int): Количество ошибок, которые можно допустить

    Returns:
        После каждой введенной буквы выводится карказ слова,
        если буква верна, то она появляется в карказе,
        если нет, то колличество ошибок увеличивается

    Raises:
        ValueError: Если введен текст неправильного формата
    """
    popыtka = 0
    print(f'Количество ошибок: {oshibki}')
    itog = ['-'] * len(slovo)
    itog1 = ''
    while popыtka != oshibki or len(itog1) != len(slovo):
        a = input()
        if a in slovo:
            for i in range(len(slovo)):
                if a == slovo[i]:
                    itog[i] = a
                    itog1 += a
            print(itog)
            print(f'Допущенно ошибок: {popыtka}', f'Осталось ошибок: {oshibki - popыtka}')
        if a not in slovo:
            popыtka += 1
            print(itog)
            print(f'Допущенно ошибок: {popыtka}', f'Осталось ошибок: {oshibki - popыtka}')
        if len(itog1) == len(slovo):
            return 'Победа!!'
        if popыtka == oshibki:
            print('Вы проиграли(')
            return f'Загаданное слово: {slovo}'
print(visiliza("носорог", 11))