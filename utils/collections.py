class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def getData(self):
    return self.data

  def setData(self, data):
    self.data = data

  def getNext(self):
      return self.next

  def setNext(self, node):
    self.next = node

class LinkedList:
  def __init__(self):
    self.head = None

  def getHead(self):
    return self.head

  def setHead(self, head):
    self.head = head

  def prepend(self, data):
    newNode = Node(data)
    newNode.setNext(self.head)
    self.head = newNode

  def append(self, data):
    if(self.head is None):
      return self.prepend(data)
    currentNode = self.head
    while(currentNode.getNext() is not None):
      currentNode = currentNode.getNext()
    newNode = Node(data)
    newNode.setNext(currentNode.getNext())
    currentNode.setNext(newNode)

  def __getNodeAt(self, pos):
    if(pos <= 0):
      return self.head
    else:
      currentNode = self.head
      while(pos > 0):
        if(currentNode.getNext() is None):
          raise Exception('Position IndexOutOfBound')
        else:
          currentNode = currentNode.getNext()
        pos -= 1
      return currentNode

  def addAt(self, data, pos):
    if(pos <= 0):
      self.prepend(data)
    else:
      nodeBeforePos = self.__getNodeAt(pos-1)
      newNode = Node(data)
      newNode.setNext(nodeBeforePos.getNext())
      nodeBeforePos.setNext(newNode)

  def getAt(self, pos):
    return self.__getNodeAt(pos).getData()

  def removeAt(self, pos):
    if(pos <= 0):
      self.head = self.head.getNext()
    else:
      nodeBeforePos = self.__getNodeAt(pos-1)
      nodeBeforePos.setNext(nodeBeforePos.getNext().getNext())

  def isEmpty(self):
    if(self.head is None):
      return True
    return False

  def size(self):
    currentNode = self.head
    count = 0
    while(currentNode is not None):
      count += 1
      currentNode = currentNode.getNext()
    return count

  def toArray(self):
    res = []
    currentNode = self.head
    while(currentNode is not None):
      res.append(currentNode.getData())
      currentNode = currentNode.getNext()
    return res

  def sort(self, compareFunc = None):
    self.setHead(self.__mergeSort(self.getHead(), compareFunc))

  def __getMiddleNode(self, head):
    if head is None:
      return None

    oneStepPointer = head
    twoStepPointer = head.getNext()

    while(twoStepPointer is not None):
      twoStepPointer = twoStepPointer.getNext()
      if twoStepPointer is not None:
        oneStepPointer = oneStepPointer.getNext()
        twoStepPointer = twoStepPointer.getNext()

    return oneStepPointer

  def __sortAndMerge(self, leftNode, rightNode, compareFunc):
    if(leftNode is None):
      return rightNode
    if(rightNode is None):
      return leftNode
    compareResult = compareFunc(leftNode.getData(), rightNode.getData())
    if compareResult == -1 or compareResult == 0:
      leftNode.setNext(self.__sortAndMerge(leftNode.getNext(), rightNode, compareFunc))
      return leftNode
    else:
      rightNode.setNext(self.__sortAndMerge(leftNode, rightNode.getNext(), compareFunc))
      return rightNode

  def __mergeSort(self, head, compareFunc=None):
    if(head is None or head.getNext() is None):
      return head
    
    if compareFunc is None:
      def defaultCompare(leftData, rightData):
        if leftData < rightData:
          return -1
        elif leftData == rightData:
          return 0
        else:
          return 1
      compareFunc = defaultCompare

    middleNode = self.__getMiddleNode(head)
    rightHead = middleNode.getNext()
    middleNode.setNext(None)

    leftHeadNode = self.__mergeSort(head, compareFunc)
    rightHeadNode = self.__mergeSort(rightHead, compareFunc)

    sortedList = self.__sortAndMerge(leftHeadNode, rightHeadNode, compareFunc)
    return sortedList  