#!/usr/bin/env python3

def print_fibonacci(n):
    # Handle the edge case where n is 0 or 1
    if n <= 0:
        print("[]")
    elif n == 1:
        print("[0]")
    else:
        # Starting sequence
        fib_sequence = [0, 1]
        for i in range(2, n):
            # Append the next Fibonacci number
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        print(fib_sequence)
