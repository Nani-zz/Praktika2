def check_winners(scores: list, student_score: int):
    """
    Выявляет попал ли ученик в тройку лучших

    Args:
        scores (list): Список с количеством баллов каждого участника олимпиады
        student_score (int): Количество баллов, которое заработал Стас

    Returns:
        str: Итог, попал ли Стас в тройку лучших

    Raises:
        ValueError: Если введен текст неправильного формата

    Example:
        >> check_winners([100, 80, 70, 67], 67)
        Вы не попали в тройку победителей.

        >> check_winners([100, 80, 70, 67], 100)
        Вы в тройке победителей!
    """

    # Отсортируем список и выявим трех лучших
    sorted_scores = (sorted(scores, reverse=True))[:3]

    if student_score in sorted_scores:
        print('Вы в тройке победителей!')
    else:
        print('Вы не попали в тройку победителей.')

# Тест
check_winners([100, 80, 70, 67], 67)
check_winners([100, 80, 70, 67], 100)