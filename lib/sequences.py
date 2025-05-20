#!/usr/bin/env python3

def print_fibonacci(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        next_value = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_value)
    print(fibonacci[:n])
