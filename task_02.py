#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task02 module"""

import task_01


def fibo(count):
    """Counts Fibonacci numbers and returns a list"""
    return [x for x in task_01.xfibo(count)]
