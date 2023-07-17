class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linked_List:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def __len__(self):
        return self.length
    
    def __str__(self):
        if self.head == None:
            return "Empty List"
        
        node = self.head
        output = ""
        while node.next:
            output += str(node.data) + " -> "
            node = node.next
        return output + str(node.data)
    
    def __contains__(self,data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
        return False
    
    def appendLeft(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        
    def append(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            prev = self.head
            while prev.next:
                prev = prev.next
            prev.next = node
        self.length += 1
            
    def popLeft(self):
        if self.head == None:
            return None
        node = self.head
        self.head = self.head.next
        self.length -= 1
        return node.data
    
    def pop(self):
        if self.head == None:
            return None
        node = self.head
        if node.next == None:
            self.head = None
        else:
            while node.next:
                prev = node
                node = node.next
            prev.next = None
        self.length -= 1
        return node.data
    
    def insert(self,i,data):
        if i <= 0:
            self.appendLeft(data)
        elif i >= self.length:
            self.append(data)
        else:
            prev = self.head
            for _ in range(i-1):
                prev = prev.next
            node = Node(data)
            node.next = prev.next
            prev.next = node
            self.length += 1
            
    def remove(self,data):
        if self.head.data == data:
            self.popLeft()
            return True
        
        prev = self.head
        while prev.next:
            if prev.next.data == data:
                prev.next = prev.next.next
                self.length -= 1
                return True
            prev = prev.next
        return False
    
    def reverse(self):
        if self.length <= 1:
            return
        ahead = self.head.next
        prev = self.head
        prev.next = None
        while ahead:
            self.head = ahead
            ahead = ahead.next
            self.head.next = prev
            prev = self.head
            
            
        
            