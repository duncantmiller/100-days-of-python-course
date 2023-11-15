# Prime numbers are numbers that can only be cleanly divided by themselves and 1.

def prime_checker(number):
    result = "is" if is_prime(number) else "is not"

    print(f"{number} {result} a prime number")

def is_prime(number):
    if number == 1:
        return False
    for n in range(2, 10):
        if number != n:
            if number % n == 0:
                return False
    return True

n = int(input("Check this number: "))
prime_checker(number=n)
