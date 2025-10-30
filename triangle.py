def triangle(num):
    i=1
    des = num -1
    while i <= num:
            space_num = ((des))
            n = " "*(space_num)+i*"* "+" "*(space_num-1)
            i += 1 
            des -= 1 
            print(n)

m = int(input("Give me a number: "))
triangle(m)