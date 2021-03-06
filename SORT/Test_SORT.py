# Практичское задание sort
# Шибаева Мария Дмитриевна|  ИВТ | 2 курс | 1 подгруппа
# Задача sort
#
# ЧАСТЬ 2
#
# Реализуйте два алгоритма сортировки: методом пузырька и быструю сортировку,
# протестируйте их работу с использованием пакета hypothesis
# (возможно использовать код из лекции по тестированию) и проанализируйте время
# выполнения сортировки двумя методами с помощью модуля timeit (см. файл example_sort.py

import sort
import pytest


@pytest.mark.parametrize("a, result", [(range(10, 100), ['14', '28', '29', '35', '41',
                                                         '53', '67', '76', '82', '92']),

                                       (
                                       range(100, 1000), ['104', '117', '140', '155', '171', '208', '209', '223', '232',
                                                          '277', '280', '290', '305', '322', '334', '343', '350', '401',
                                                          '410', '433', '446', '464', '503', '515', '530', '551', '588',
                                                          '589', '598', '599', '607', '644', '668', '669', '670', '686',
                                                          '696', '706', '711', '727', '760', '772', '802', '820', '858',
                                                          '859', '866', '885', '895', '902', '920', '958', '959', '966',
                                                          '985', '995']),)])
def test_sort(a, result):
    assert sort(a) == result
