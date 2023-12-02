#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from abc import ABC
from typing import Union, Self


class Number(ABC):
    """
    Абстрактный класс для числа
    """
    def __init__(self, value: Union[int, float]):
        self.value = value

    def add(self, other: Self):
        """
        Операция сложения
        """
        self.value = self.value + other.value

    def sub(self, other: Self):
        """
        Операция вычитания
        """
        self.value = self.value - other.value

    def mul(self, other: Self):
        """
        Операция умножения
        """
        self.value = self.value * other.value

    def div(self, other: Self):
        """
        Операция деления
        """
        self.value = self.value / other.value

    def __str__(self):
        return str(self.value)


class Integer(Number):
    """
    Класс "Целочисленное значение", наследуется от базового класса для всех чисел
    """
    def __init__(self, value: int):
        super().__init__(value)

    def add(self, other: Self):
        """
        Переопределенный метод сложения
        """
        self.value = int(self.value + other.value)

    def sub(self, other: Self):
        """
        Переопределенный метод вычитания
        """
        self.value = int(self.value - other.value)

    def mul(self, other: Self):
        """
        Переопределенный метод умножения
        """
        self.value = int(self.value * other.value)

    def div(self, other: Self):
        """
        Переопределенный метод деления
        """
        self.value = int(self.value / other.value)


class Real(Number):
    """
    Класс "Дробное число", наследуется от базового класса для всех чисел
    """
    def __init__(self, value: float):
        super().__init__(value)


if __name__ == "__main__":
    # Создадим число 10
    int1 = Integer(10)

    # Добавим к нему число 5
    int1.add(Integer(5))
    print(int1)

    # Разделим на 3
    int1.div(Integer(3))
    print(int1)

    # Умножим на 5
    int1.mul(Integer(5))
    print(int1)

    # Вычтем 10
    int1.sub(Integer(10))
    print(int1)

    # Создадим дробное число 10.5
    real1 = Real(10.5)

    # Добавим к нему другое дробное число 5.5
    real1.add(Real(5.5))
    print(real1)

    # Вычтем 3.5
    real1.sub(Real(3.5))
    print(real1)

    # Разделим на 2.5
    real1.div(Real(2.5))
    print(real1)

    # Умножим на 4.8
    real1.mul(Real(4.8))
    print(real1)
