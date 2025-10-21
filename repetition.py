my_list = [1,3,3,4,5,6,6,7,7]

not_dup = set()
dup  = set()

for num in my_list:
    if num in not_dup:
        dup.add(num)
    else:
        not_dup.add(num)

print(list(dup))


