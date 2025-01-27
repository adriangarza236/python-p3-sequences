#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        return print([])
    elif length == 1:
        return print([0])
    elif length == 2:
        return print([0, 1])
    else:
        fib_seq = [0, 1]
        while len(fib_seq) < length:
            next_term = fib_seq[-1] + fib_seq[-2]
            fib_seq.append(next_term)
        return print(fib_seq)
