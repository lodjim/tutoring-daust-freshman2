
# list_of_integer = [1,2,53,6,3,66,4,4,7,8,3,6,9]
# set_of_odds = set()
# for integer in list_of_integer:
#     if integer%2 != 0:
#         set_of_odds.add(integer)
# for i in range(len(list_of_integer)):
#     integer = list_of_integer[i]
#     if integer not in list(set_of_odds):
#         list_of_integer[i] = list_of_integer[i]**2
# print(list_of_integer)


# list_of_integer = [1,2,53,6,3,66,4,4,7,8,3,6,9]
# set_of_odds = set()


# for j in range(len(list_of_integer)-1):  
#         integer = list_of_integer[j]
#         if integer%2 != 0:
#             list_of_integer.remove(integer)
   
# print([integer**2 for integer in list_of_integer])


list_of_integer = [1,2,53,6,3,66,4,4,7,8,3,6,9]
i = 0
while i < len(list_of_integer):
    integer = list_of_integer[i]
    if integer%2 != 0:
        list_of_integer.remove(integer)    
    else:
        list_of_integer[i] = integer**2
    i += 1 

print(list_of_integer)

