import time


list_ex = [item for item in range(100)]
set_ex = set(list_ex)

start_list = time.time()
bool_1 = 99 in list_ex
end_list = time.time() - start_list
print('bool_1: ', bool_1)
print('set took: ', end_list)



start_set = time.time()
bool_2 = 99 in set_ex
end_set = time.time() - start_set
print('bool_2: ', bool_2)
print('set took: ', end_set)


diff = (end_set-end_list) / end_list


print('percentage difference: ', diff * 100)

