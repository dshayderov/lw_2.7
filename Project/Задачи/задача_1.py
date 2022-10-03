#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # Определим универсальное множество
    gl = set("aeyuioаеёиоуыэюя")

    s = set(input("Введите строку:\n").lower())

    x = len(s.intersection(gl))
    print(f"Кол-во гласных в строке: {x}")