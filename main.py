from math import sqrt

while True:
    a = int(input("Give me the value of a: "))
    b = int(input("Give me the value of b: "))
    c = int(input("Give me the value of c: "))

    if a == 0 :
        print("a cannot be equal to zero")
        continue
    
    delta = b**2-(4*a*c)

    if delta < 0:
        print("impossible in R")

    elif delta > 0 :
        r1 = (-b-sqrt(delta))/(2*a)
        r2 = (-b+sqrt(delta))/(2*a)
        print("R1:",r1)
        print("R2:",r2)
    else :
        r = (-b)/(2*a)
        print("R:",r)

    