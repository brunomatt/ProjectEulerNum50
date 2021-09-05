# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
import time
start = time.time()

iterations = []
answers = []
primes = []

def sieve_eratosthenes(n):
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return primes

sieve_eratosthenes(1000000)
max_counter = 0

for prime_number in primes:
    if prime_number < 50000:
        prime_index = primes.index(prime_number)
        check = prime_number
        counter = 1
        while check < 1000000:
            check += primes[prime_index + counter]
            counter += 1
            if check in primes:
                if counter > max_counter:
                    iterations.append(counter)
                    answers.append(check)

answer = answers[iterations.index(max(iterations))]
print(answer)

stop = time.time()
print(stop - start, 'secs')