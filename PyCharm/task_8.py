#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Инициализация множества гласных
    vowels = {'а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е'}
    # Вводимая строка
    s = input("Enter the string: ").lower()
    # Создание листа с гласными из строки
    v_list = [i for i in s if i in vowels]
    # Результат
    print(f"The number of vowels in the string: {len(v_list)}")
    print(v_list)
