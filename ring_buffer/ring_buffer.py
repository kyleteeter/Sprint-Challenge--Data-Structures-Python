class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # Base case for self.current
    if self.current == self.capacity:
      self.current = 0
    # If self.storage at index is none remove
    if self.storage[self.current] == None:
      self.storage.pop(self.current)
      self.storage.insert(self.current, item)
      self.current += 1
    else:
      self.storage.pop(self.current)
      self.storage.insert(self.current, item)
      self.current += 1



  def get(self):
    # Create store
    store_list = list(self.storage)
    # check to see if None exists
    i = 0
    for i in store_list:
      # Remove any nones found
      if i is None:
        store_list.remove(None)
    return store_list