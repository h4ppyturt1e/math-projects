with open('prime_numbers.txt') as f:
    prime_list = [int(line.split(', ')[1]) for line in f.readlines()]

numbers = input('Enter list of numbers, eg. 3,19,4,9')
numbers = numbers.split(',')
numbers = [int(number) for number in numbers]

print('Input:\n{}\n'.format(numbers))

if not any(x > prime_list[-1] for x in numbers):
    loprime_factors = []

    for number in numbers:
        prime_factors = []

        for prime in prime_list:
            while number != 1:
                if number % prime == 0:
                    prime_factors.append(prime)
                    number /= prime
                else:
                    break
            if number == 1:
                break
        loprime_factors.append(prime_factors)
    print('List of prime factors for each number:\n{}\n'.format(loprime_factors))

    lodicts = []
    loprimes = []
    for prime_factors in loprime_factors:
        num_dict = {}
        
        for prime in prime_factors:
            if prime not in num_dict:
                num_dict[prime] = 1
            else:
                num_dict[prime] += 1
            if prime not in loprimes:
                loprimes.append(prime)
        lodicts.append(num_dict)
    print('List of prime factorization of each number:\n{}\n'.format(lodicts))

    lowest_primes = {prime: 0 for prime in loprimes}
    for prime_dict in lodicts:
        for prime in loprimes:
            if prime in prime_dict and lowest_primes[prime] <= 0:
                lowest_primes[prime] = prime_dict[prime]
    print('Lowest prime factorization:\n{}\n'.format(lowest_primes))

    total = 1
    for prime in lowest_primes:
        total *= (prime ** lowest_primes[prime])

    print('LCM of {} is {}'.format(numbers, total))
else:
    print('Number is too large, unable to compute.')