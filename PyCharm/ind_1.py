#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")
    # Инициализация множеств
    A = {'c', 'm', 'n', 'o', 'q'}
    B = {'c', 'd', 'm', 'w'}
    C = {'m', 'n', 'q'}
    D = {'c', 'm', 'p'}
    # Найдем дополнения множества
    Bn = u.difference(B)
    # Проверка и вывод
    print(f"Step_1, A⋃B: {A.union(B)}")
    print(f"Step_2,(A⋃B)∩С:  {(A.union(B)).intersection(C)}")
    print(f"X = {(A.union(B)).intersection(C)}")
    print("------------------------------------------------")
    print(f"Step_1, A∩¬B: {A.intersection(Bn)}")
    print(f"Step_2,С/D: {(C.difference(D))}")
    print(f"Step_3,(A∩ ¬B)⋃(С/D): {(A.intersection(Bn)).union(C.difference(D))}")
    print(f"Y = {(A.intersection(Bn)).union(C.difference(D))}")
