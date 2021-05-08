import math


def check_prime(number):
    for num in range(2, int(math.sqrt(number) + 1)):
        if number % num == 0:
            return False
    return True


def generate_prime_numbers(boundary, prime_numbers):
    for num in range(2, boundary):
        if check_prime(num):
            prime_numbers.append(num)


def count_goldbach_combinations(boundary, prime_numbers):
    answer = []
    for num in range(4, boundary, 2):
        count = 0
        minor_prime_index = 0
        while prime_numbers[minor_prime_index] <= num / 2:
            if (num - prime_numbers[minor_prime_index]) in prime_numbers:
                count += 1
            minor_prime_index += 1
        answer.append(count)
    return answer


prime_numbers = []
boundary = 1000
generate_prime_numbers(boundary, prime_numbers)
answer = count_goldbach_combinations(boundary, prime_numbers)
print(answer)
