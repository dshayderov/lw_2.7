#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"a", "b", "d", "i", "x"}
    b = {"d", "e", "h", "i", "n", "u"}
    c = {"e", "f", "m", "n"}
    d = {"a", "c", "h", "k", "r", "s", "w", "x"}

    an = u - a
    bn = u - b

    x = (a - c) & bn
    print(f"x = {x}")

    y = (an & d) | (c - b)
    print(f"y = {y}")