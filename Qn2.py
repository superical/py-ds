from random import randint
import math
import operator
import time
start = time.clock()

data = []
for i in range(0, 10):
  data.append(randint(0, 100))

print('Data:', data)
data.sort()
print('Sorted Data:', data)
print('\n')

def binary_search(data, target):
  if len(data) == 0:
    return False
  if len(data) == 1:
    return data[0] == target
  mid = math.floor(len(data) / 2)
  if data[mid] == target:
    return True
  elif target < data[mid]:
    return binary_search(data[:mid], target)
  else:
    return binary_search(data[mid+1:], target) 

#searchNum = 177
searchNum = randint(0, 100)
existingNum = data[randint(0, len(data)-1)]
print('Does the list contain {}? {}'.format(searchNum, binary_search(data, searchNum)))
print('Does the list contain {}? {}'.format(existingNum, binary_search(data, existingNum)))

print('Time taken to execute:', time.clock() - start)
