def bubbleSortRecursive(list):
  def bbsort(list, i, j):
    if i == 0:
      return list
    else:
      if list[j] > list[j+1]:
        temp = list[j]
        list[j] = list[j+1]
        list[j+1] = temp
      j += 1
      if j == i:
        j = 0
        i -= 1
      return bbsort(list, i, j)
  return bbsort(list[:], len(list)-1, 0)  #immutable

from random import randint
list = []
for i in range(0, 10):
  list.append(randint(0, 100))
print('Before sort:', list)

print('After sort:', bubbleSortRecursive(list))