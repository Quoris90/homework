immutable_var = (5, 'me', True, 5.0 )
print(immutable_var)
# immutable_var[1] = 10
# print(immutable_var) #потому что, данные в кортеже не изменяются

mutable_list = [2, True, 'banana', 2.1]
while len(mutable_list) == 4:
    mutable_list = immutable_var[:: -1]
    break

print(mutable_list)
