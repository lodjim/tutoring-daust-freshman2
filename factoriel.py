
# n! = n*(n-1)*...*1


n = 10
result = 1
for i in range(n-1):
    result *= n-i
    #result = result * (n-i)
print(result)


def factoriel(n):
    if n == 0:
        return 1 
    if n == 1:
        return 1
    return n * factoriel(n-1)

result = factoriel(10)

print(result)