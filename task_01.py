#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task01 module"""


def xfibo(count):
    a, b = 0, 1
    res = [a]
    iter = 1
    while count > iter:
        res.append(b)
        a, b = b, a + b
        iter = iter + 1

    return res
