# Практичское задание NOD
# Шибаева Мария Дмитриевна|  ИВТ | 2 курс | 1 подгруппа
# Задача NOD
#
# ЧАСТЬ 2
#
# Напишите программу, которая реализует нахождение наибольшего общего делителя двух чисел A, B
# Тесты оформите с помощью pytest или UnitTest.

import pytest

import nod

def factory(a, b, c):
	def test():
		assert nod.nod(a, b) == c
	return test


test1 = factory(1, 11, 1)
test2 = factory(5, 55, 5)
test3 = factory(12345, 123, 3)
