from math import sqrt

def is_prime_number(number):
    start = 2
    end = int(sqrt(number))
    list_of_candidates = list(range(start,end+1))
    for candidate in list_of_candidates:
        if number%candidate == 0:
            return "Not a prime number"
    return "This is a prime number"

results = is_prime_number(3)

print(results)



# 10 
