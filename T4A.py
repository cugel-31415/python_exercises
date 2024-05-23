def calc_range(num, divisor):
    check_range = num // divisor
    if check_range % 2 == 0:
        check_range += 1

    return check_range


def is_prime(num):
    # basic tests
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    # check all the odd numbers that are prime whether the number can be divided by them
    # every failed check decreases the range to check
    divisor = 3
    check_range = calc_range(num, 2)
    while divisor < check_range:
        # recursive call, we don't need to check non-prime numbers
        if not is_prime(divisor):
            divisor += 2
            continue

        if num % divisor == 0:
            return False
        
        check_range = calc_range(num, divisor)

        # only odd numbers need to be checked
        divisor += 2
        
    # it must be prime
    return True

result = [" ", " not "]
result_idx = 0
primes = []
for num in range(1, 51):
    if is_prime(num):
        result_idx = 0
        primes.append(num)
    else:
        result_idx = 1

    print("{} is{}prime".format(num, result[result_idx]))

print("List of primes from 1 - 50:", primes)

# With this test I measured the speed of my algorithm. It took 1 minute and 25 seconds to run
#
# for num in range(500000):
#     if is_prime(num):
#         print(num)
 