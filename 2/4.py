import time
import math

def primes1(to):
    primes = [2]
    for i in range(3, to, 2):
        prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if (i % j == 0):
                prime = False
        if prime:
           primes.append(i)
    return primes

def primes2(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            primes.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return primes

def primes3(n):
    sieve = [True] * int(n / 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[int(i / 2)]:
            sieve[int(i * (i / 2))::i] = [False] * int((n - i * i - 1) / (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, int(n / 2)) if sieve[i]]

def primes4(n):
    primes = [2]
    sieve = [True] * int(n / 2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if sieve[int(i / 2)]:
            sieve[int(i * (i / 2))::i] = [False] * int((n - i * i - 1) / (2 * i) + 1)
    for i in range(1, int(n / 2)):
        if sieve[i]:
            primes.append(2 * i + 1)
    return primes

start_time = time.time()

# primes = primes1(1000000) # 34 seconds
# primes = primes2(1000000) # 0.4 seconds
# primes = primes3(1000000) # 0.07 seconds
primes = primes4(1000000) # 0.07 seconds

done_in = time.time() - start_time

for i in primes:
    print(i)

print(done_in, 'seconds')
print('Checksum:', len(primes) == 78498, '=', len(primes))
