import time

start_time = time.time()

print('Timing for loop')
_sum = 0
_list = []
for i in range(10):
    _list.append(i)
_sum = sum(_list)
print('For loop took %s', time.time() - start_time)
print('Result: ',_sum)

start_time = time.time()
print('Timing list comprehension')
_sum = 0
_list = [n for n in range(10)]
_sum = sum(_list)
print('List comprehension took %s', time.time() - start_time)
print('Result:' ,_sum)


start_time = time.time()
print('Timing generator expression')
_sum = 0
_gen = (n for n in range(10))
_list = list(_gen)
_sum = sum(_list)
print('List using generator took %s', time.time() - start_time)
print('Result: ', _sum)


start_time = time.time()
print('Timing generator inside the sum')
_sum = sum(n for n in range(10))
print('Generator directly inside sum took %s', time.time() - start_time)
print('Result: ', _sum)



