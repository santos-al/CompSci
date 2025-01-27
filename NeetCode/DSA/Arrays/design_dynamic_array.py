class DynamicArray:

  # O(n) -> n = capacity
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.size = 0
    self.arr = [0] * capacity

  # O(1)
  def getCapacity(self) -> int:
    return self.capacity
  
  # O(1)
  def getSize(self) -> int:
    return self.size
  
  # O(1)
  def get(self, i: int) -> int:
    if i >= self.size:
      raise IndexError
    return self.arr[i]
  
  #  O(1)
  def insert(self, i: int, n: int) -> None:
    if i >= self.size:
      raise IndexError
    self.arr[i] = n
  
  # O(n) -> if we need to resize, if not then O(1) which is the average, amortized time complexity
  def pushback(self, n: int) -> None:
    if self.self == self.capacity:
      self.resize()
    self.arr[self.size] = n
    self.size += 1

  # O(1)
  def popback(self) -> int:
    if self.size == 0:
      raise IndexError 
    # Soft deletes the item in the array
    self.size -= 1
    return self.arr[self.size]
  
  # O(n)
  def resize(self) -> None:
    self.capacity = self.capacity * 2
    new_arr = [0] * self.capacity

    for i in range(self.size):
      new_arr[i] = self.arr[i]
    
    self.arr = new_arr
