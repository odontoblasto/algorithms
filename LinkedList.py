class Node:
    def __init__(self, next = None, value = None):
      self.next = next
      self.value = value
  
class LinkedList:
    def __init__(self,head = None):
      self.head = head
    
    #create a LIFO(last in,first out)- Stack
    def addNode(self,value):
      self.head = Node (self.head,value)
      return self.head
    #create a FIFO(first in,first out)- List or Array
    def addNode(self,value):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(next,value)
            return pointer.next # or Node(next,value)
        self.head = Node(self.head,value)
        return self.head # or Node(next,value)
