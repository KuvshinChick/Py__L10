#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Ввод строк
    s = set(input("Enter the first string: ").lower())
    s_1 = set(input("Enter the second string: ").lower())
    # Вывод пересечения множеств
    print(f"Common symbols: { s.intersection(s_1)}")
