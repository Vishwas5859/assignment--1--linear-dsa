
#Q1. Delete the elements in an linked list whose sum is equal to zero

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#class Linked List
class LinkedList:
  def __init__(self):
    self.head = None

  #Add new element at the end of the list
  def push_back(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return
    else:
      temp = self.head
      while(temp.next != None):
        temp = temp.next
      temp.next = newNode

  #Delete an element at the given position
  def pop_at(self, position):     
    if(position < 1):
      print("\nposition should be >= 1.")
    elif (position == 1 and self.head != None):
      nodeToDelete = self.head
      self.head = self.head.next
      nodeToDelete = None
    else:    
      temp = self.head
      for i in range(1, position-1):
        if(temp != None):
          temp = temp.next   
      if(temp != None and temp.next != None):
        nodeToDelete = temp.next
        temp.next = temp.next.next
        nodeToDelete = None 
      else:
        print("\nThe node is already null.") 

  #display the content of the list
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

# test the code                
MyList = LinkedList()

#Add three elements at the end of the list.
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.PrintList()

#Delete an element at position 2
MyList.pop_at(2)
MyList.PrintList()

#Delete an element at position 1
MyList.pop_at(1)
MyList.PrintList() 
#--------------------------------------------------------------------------------------------

# Q2 Reverse a linked list in groups of given size:
class ListNode:
   def __init__(self, data, next = None):
      self.val = data
      self.next = next
def make_list(elements):
   head = ListNode(elements[0])
   for element in elements[1:]:
      ptr = head
      while ptr.next:
         ptr = ptr.next
      ptr.next = ListNode(element)
   return head
def print_list(head):
   ptr = head 
   print('[', end = "")
   while ptr:
      print(ptr.val, end = ", ")
      ptr = ptr.next
      print(']')
class Solution:
   def solve(self, node, k):
      tmp = ListNode(0)
      tmp.next = node
      prev, curr = None, node
      lp, lc = tmp, curr
      cnt = k
      while curr:
         prev = None
         while cnt > 0 and curr:
            following = curr.next
            curr.next = prev
            prev, curr = curr, following
            cnt -= 1
         lp.next, lc.next = prev, curr
         lp, lc = lc, curr  
         cnt = k
      return tmp.next
ob = Solution()
head = make_list([1,2,3,4,5,6,7,8,9,10])
print_list(ob.solve(head, 3)) 
#----------------------------------------------------------------------------------------

#Q3. Merge a linked list into another linked list at alternate positions.

class Node(object):
    def __init__(self, data:int):
        self.data = data
        self.next = None
  
  
class LinkedList(object):
    def __init__(self):
        self.head = None
          
    def push(self, new_data:int):
        new_node = Node(new_data)
        new_node.next = self.head
        
        self.head = new_node
          
    
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
              
    
    def merge(self, p, q):
        p_curr = p.head
        q_curr = q.head

        while p_curr != None and q_curr != None:
  
            
            p_next = p_curr.next
            q_next = q_curr.next
  
            
            q_curr.next = p_next 
            p_curr.next = q_curr  
  
            
            p_curr = p_next
            q_curr = q_next
            q.head = q_curr

llist1 = LinkedList()
llist2 = LinkedList()
  
llist1.push(3)
llist1.push(2)
llist1.push(1)
llist1.push(0)
  
for i in range(8, 3, -1):
    llist2.push(i)
  
print("First Linked List:")
llist1.printList()

print("First Linked List:")
llist1.printList()
  
print("Second Linked List:")
llist2.printList()
  
llist1.merge(p=llist1, q=llist2)
  
print("Modified first linked list:")
llist1.printList()
  
print("Modified second linked list:")
llist2.printList()
#----------------------------------------------------------------------------------------

# Q4 In an array, Count Pairs with given sum

def getPairsCount(arr, n, K):
    count = 0  
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == K:
                count += 1
 
    return count

arr = [1, 5, 7, -1]
n = len(arr)
K = 6
print("Count of pairs is: ",getPairsCount(arr, n, K))
#--------------------------------------------------------------------------------------------------

# Q5. Find duplicates in an array
arr = [1, 2, 3, 4, 2, 7, 8, 8, 3];     
     
print("Duplicate elements in given array: ")     
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            print(arr[j])    

#---------------------------------------------------------------------------------------------------
# Q6. Find the Kth largest and Kth smallest number in an array

def find(k, arr, l):
    arr.sort(reverse=True)
    print("K th maximum element is: ", arr[k - 1])
    print("K th minimum element is: ", array[l - k])


array = [1, 7, 6, 8, 9, 2, 4, 5, 3, 0]
k = 2
find(k, array, len(array)) 

#---------------------------------------------------------------------------------------------------
#Q7. Move all the negative elements to one side of the array
def find(arr):
    arr.sort(reverse=True)
    print("Array after moving all the elements to right:", arr)


array = [1, 3, -1, 4, -3, -5, -6, 3, 7]
find(array) 
#-------------------------------------------------------------------------------------------------
#Q8. Reverse a string using a stack data structure
def createStack():
    stack = []
    return stack
  
def size(stack):
    return len(stack)
  
def isEmpty(stack):
    if size(stack) == 0:
        return True
 
def push(stack, item):
    stack.append(item)
  
def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()

def reverse(string):
    n = len(string)
    
    stack = createStack()
    
    for i in range(0, n, 1):
        push(stack, string[i])
    string = ""
    for i in range(0, n, 1):
        string += pop(stack)
 
    return string

string = "Edyoda"
string = reverse(string)
print("Reversed string is " + string)

#------------------------------------------------------------------------------------------------
# Q9. Evaluate a postfix expression using stack

class evaluate_postfix:
    def __init__(self):
        self.items=[]
        self.size=-1
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
        self.size+=1
    def pop(self):
        if self.isEmpty():
            return 0
        else:
            self.size-=1
            return self.items.pop()
    def seek(self):
        if self.isEmpty():
            return False
        else:
            return self.items[self.size]
    def evalute(self,expr):
        for i in expr:
            if i in '0123456789':
                self.push(i)
            else:
                op1=self.pop()
                op2=self.pop()
                result=self.cal(op2,op1,i)
                self.push(result)
        return self.pop()
    def cal(self,op2,op1,i):
        if i is '*':
            return int(op2)*int(op1)
        elif i is '/':
            return int(op2)/int(op1)
        elif i is '+':
            return int(op2)+int(op1)
        elif i is '-':
            return int(op2)-int(op1)
s=evaluate_postfix()
expr=input('enter the postfix expression')
value=s.evalute(expr)
print('the result of postfix expression',expr,'is',value)
#--------------------------------------------------------------------------------------------

#Q10. Implement a queue using the stack data structure
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def enQueue(self, x):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s1.pop()
        self.s1.append(x)
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def deQueue(self):
        if len(self.s1) == 0:
            return -1
        x = self.s1[-1]
        self.s1.pop()