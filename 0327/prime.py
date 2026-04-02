n_primes = 50
number = 2
count = 0

while count < n_primes:
    divisor = 2
    prime = True

    while divisor < number:
        if number % divisor == 0:
            prime = False
            break
        divisor += 1
    if prime:
        count += 1
        print(number, end=" ")
    number += 1