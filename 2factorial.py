def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))


recursive_result = factorial_recursive(num)
iterative_result = factorial_iterative(num)


print(f"Factorial of {num} using recursion: {recursive_result}")
print(f"Factorial of {num} using iteration: {iterative_result}")