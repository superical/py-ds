from random import sample, randint

class Stack:

  def __init__(self):
    self.stack = []

  def push(self, item):
    self.stack.append(item)

  def pop(self, position=-1):
    return self.stack.pop(position)

  def peek(self, position=-1):
    return self.stack[position]

  def size(self):
    return len(self.stack)

  def isEmpty(self):
    return self.stack == [] or len(self.stack) == 0

  def __iter__(self):
    self.iter_idx = 0
    return self

  def __next__(self):
    if self.iter_idx >= len(self.stack):
      raise StopIteration
    curr_idx = self.iter_idx
    self.iter_idx += 1
    return self.stack[curr_idx]


def pprint_gifts(gift_stack):
  print('\n'.join(['{} - {}'.format(idx+1, gift) for idx, gift in enumerate(gift_stack)]))

gifts = Stack()
gifts.push('iPhone XS')
gifts.push('Wireless Headphones')
gifts.push('Stuffed Bunny Toy')
gifts.push('Nike Cap')
gifts.push('Silver Heart Pendant')
gifts.push('Happy Birthday Photo Frame')
gifts.push('Gadget Key Chain')
gifts.push('Smart Watch')

print('~ Mystery Gift Vending Machine ~')
pprint_gifts(gifts)

print('\n')

def rand_gift_ids(gift_size, quantity):
  return sample(range(0, gift_size), quantity)

mystery_gift_ids = rand_gift_ids(gifts.size(), 3)

mystery_gifts = [gifts.peek(gift_id) for gift_id in mystery_gift_ids]
print('You will get one of these gifts below.')
pprint_gifts(mystery_gifts)
print('\n')

selected_gift_id = mystery_gift_ids[randint(0, len(mystery_gift_ids)-1)]

print('Your mystery gift is', gifts.peek(selected_gift_id))
print('\n')

gifts.pop(selected_gift_id)
print('Here are the remaining gifts.')
pprint_gifts(gifts)