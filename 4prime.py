def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(start, end):
    """Find and print all prime numbers in the range [start, end]."""
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Find and print all primes in the given range
print(f"Prime numbers between {start} and {end}:")
find_primes(start, end)