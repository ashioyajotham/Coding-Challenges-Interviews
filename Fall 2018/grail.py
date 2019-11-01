#print("Hello")



# Your last C/C++ code is saved below:
# #include <iostream>
# using namespace std;

# int main() {
# 	cout<<"Hello";
# 	return 0;
# }

class Stack:

  def __init__(self):
    self.array = []

  
  def push(self, input):
    self.array += [input]
  
  def pop(self):
    if self.array == []:
      return None

    result = self.array[-1]

    self.array = self.array[:-1]

    return result

  def peek(self):

    if self.array == []:
      return None

    return self.array[-1]

class Stack2:

  def __init__(self):
    self.array = [None] * 1000
    self.index = -1
    self.stackMax = -float('inf')
    self.maxStack = [None] * 1000
    self.maxIndex = -1

  
  def push(self, input):
    # if input in self.data:
    #   return

    

    self.index += 1
    self.array[self.index] = input
    #self.data.add(input)

    if self.maxIndex == -1 or (self.maxIndex >= 0 and self.maxStack[self.maxIndex] < input):
      self.maxIndex += 1
      self.maxStack[self.maxIndex] = input
    else:
      currentMax = self.maxStack[self.maxIndex]
      self.maxIndex += 1
      self.maxStack[self.maxIndex] = currentMax


    # if input > self.stackMax:
    #   self.stackMax = input
  
  def pop(self):
    if self.index == -1:
      return None

    result = self.array[self.index]
    self.index -= 1
    # self.data.remove(result)

    self.maxIndex -= 1
    
    return result

  def peek(self):
    if self.index == -1:
      return None

    return self.array[self.index]
  
  def getMax(self):
    return self.maxStack[self.maxIndex]
  
  

def test():
  stack = Stack2()

  stack.push(1)
  result = stack.peek()
  print(result)

  stack.push(2)

  result = stack.pop()

  print(result)

#test()

def test2():
  stack = Stack2()

  result = stack.pop()

  print(result)

#test2()

def test3():
  stack = Stack2()

  stack.push(5)
  stack.push(4)
  stack.push(3)
  
  result = stack.getMax()
  print(result)

  stack.pop()
  result = stack.getMax()
  print(result)

test3()


