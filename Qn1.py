def invInsertionSort(list):
    for index in range(len(list)-1, -1, -1):
        currentvalue = list[index]
        position = index

        while position >= 0 and position < len(list)-1 and list[position + 1] > currentvalue:
            list[position] = list[position + 1]
            position = position + 1

        list[position] = currentvalue


from random import randint

def main():
  list = []
  for i in range(0, 10):
    list.append(randint(0, 100))
  print('Before sort:', list)

  invInsertionSort(list)
  print('After sort:', list)

if __name__ == '__main__':
  main()