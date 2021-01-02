def generate_fibonacci(boundary):
    # This function generates a fibonacci sequence,
    # starting with 1 & 2 ending at a value not greater than the boundary specified by the argument.

    fibonacci = [1, 2]
    while fibonacci[-1] < boundary:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    fibonacci_evens = [x for x in fibonacci if x % 2 == 0]
    return sum(fibonacci_evens)


print(generate_fibonacci(4000000))
