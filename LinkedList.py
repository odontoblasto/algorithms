class Node:
    def __init__(self, next = None, value = None):
      self.next = next
      self.value = value
  
class LinkedList:
    def __init__(self,head = None):
      self.head = head
    
    def addNode(self,value):
      self.head = Node (next,value)
      return self.head
