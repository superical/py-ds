from functools import reduce
from random import randint, shuffle
import operator
import time
start = time.clock()

class Node:

  value = 0
  left = None
  right = None

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, node):
    if node.value < self.value:
      if self.left == None:
        self.left = node
        return self.left
      else:
        self.left.insert(node)
    else:
      if self.right == None:
        self.right = node
        return self.right
      else:
        self.right.insert(node)

  def contains(self, node):
    if node.value == self.value:
      return True
    else:
      if node.value < self.value:
        if self.left == None:
          return False
        return self.left.contains(node)
      else:
        if self.right == None:
          return False
        return self.right.contains(node)

  def traverse(self):
    subres_left = []
    subres_right = []
    if self.left != None:
      subres_left = self.left.traverse()
    if self.right != None:
      subres_right = self.right.traverse()
    return reduce(operator.concat, [subres_left, [self.value], subres_right])



data = []
for i in range(0, 10):
  data.append(randint(0, 100))

tree = Node(data[0])
for i in range(1, 10):
  tree.insert(Node(data[i]))

to_list = tree.traverse()

print(to_list)

#searchNum = 177
searchNum = randint(0, 100)
existingNum = data[randint(0, len(data)-1)]
print('Does the tree contain {}? {}'.format(searchNum, tree.contains(Node(searchNum))))
print('Does the tree contain {}? {}'.format(existingNum, tree.contains(Node(existingNum))))

print('Time taken to execute:', time.clock() - start)