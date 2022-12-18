# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 19:27:57 2022

@author: Yuanyuan_Tang

Data structure practice in Python
https://www.edureka.co/blog/data-structures-in-python/

https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

"""


import numpy as np


'''
Data structure: list
'''
print('------------------------------List--------------------------')
a=[]
print('a=',a)
b=[1,'1',2,'2','Hellow world!']
print('b=',b)

print('Positive index: b[3]=',b[3])
print('Negative index: b[-1]=',b[-1])


b.append([555, 12]) #add as a single element
print('Append [555, 12], b=',b)
b.extend([234, 'more_example']) #add as different elements
print('add another two elements, b=',b)
print('Lenght of b is', len(b)) # Length of b


for element in b: #access elements one by one
    print(element)

print(b[0]==b[1])

my_list = [1, 2, 3, 'example', 3.132, 10, 30]
del my_list[5] #delete element at index 5
print(my_list)
my_list.remove('example') #remove element with value
print(my_list)
a = my_list.pop(3) #pop element from index 1 of list 
print('Popped Element: ', a, ' List remaining: ', my_list)
my_list.clear() #empty the list
print(my_list)


my_list = [1, 2, 3, 10, 30, 10]
print(len(my_list)) #find length of list
print(my_list.index(10)) #find index of element that occurs first
print(my_list.count(10)) #find count of the element
print(sorted(my_list)) #print sorted list but not change original
my_list.sort(reverse=True) #sort original list in descent order
print(my_list)

'''
Data structure: dictionary
'''
print('------------------------------dictionary--------------------------')
mydict={}
print(mydict)
mydict={1:'python', 2:'C'}
print(mydict)

mydict[3]='Java' # insert key-value pair
print('Insert a pair 3:Java, mydict=', mydict)

my_dict = {'First': 'Python', 'Second': 'Java'}
print(my_dict)
my_dict['Second'] = 'C++' #changing element
print(my_dict)


my_dict = {1: 'Python', 2: 'Java', 3: 'Ruby'}

print('my_dict[3]=', my_dict[3])


print('keys=:',my_dict.keys()) #get keys
print('Values:',my_dict.values()) #get values
b=my_dict.items()
print('Key-value pairs:', b) #get key-value pairs
for e in b:
    print(e[0], e[1])

a=my_dict.pop(1)
print('Value:', a)
print('Dictionary:', my_dict)
b = my_dict.popitem() #pop the key-value pair
print('Key, value pair:', b)
print('Dictionary', my_dict)
my_dict.clear() #empty dictionary
print('n', my_dict)


'''
Data structure: tuple
'''
print('------------------------------tuple--------------------------')

mytuple=(1,2,3) #create tuple
print('mytuple=:',mytuple) 

print('Show each element')
for e in mytuple:
    print(e)
    
print(mytuple[1])  # Get access one element

mytuple=mytuple+(5,6,7) # add elements
print('Add elements 5,6,7, mytuple=:',mytuple)
print(mytuple.count(2))# Frequency of 2
print(mytuple.index(5))   # Index of 2


'''
Data structure: set
'''
print('------------------------------set--------------------------')

my_set = {1, 2, 3, 4, 5, 5, 5} #create set
print(my_set)

my_set.add(4) #add element to set
print(my_set)


my_set = {1, 2, 3, 4}
my_set_2 = {3, 4, 5, 6}
print(my_set.union(my_set_2), '----------', my_set | my_set_2)
print(my_set.intersection(my_set_2), '----------', my_set & my_set_2)
print(my_set.difference(my_set_2), '----------', my_set - my_set_2)
print(my_set.symmetric_difference(my_set_2), '----------', my_set ^ my_set_2)
my_set.clear()
print(my_set)


'''
Data structure: LinkedList
'''
print('------------------------------Linkedlist--------------------------')


class Node:    
   def __init__(self, val=None): #Pay attention to the 
   #function __init__(self, val=None) with long "__"
       self.val=val
       self.next=None

#p=Node(None)
a=[1,2,3,4,5]

print("Input data a=:",a)

m=len(a)
header=S_link=Node(None)
#S_link.next=Node(1)
for i in range(m):
    S_link.next=Node(a[i])
    S_link=S_link.next
    
print("print the linkedlist")
header=header.next
while(header):
    print(header.val)
    header=header.next



'''
Data structure:tree
'''
print('------------------------------Tree--------------------------')

class node:
    def __init__(self, val=None):
        self.val=val
        self.left=None
        self.right=None


root=node(3)
print("root.val=", root.val)

List_tree=[3,2,4,5,6,7]

root=tree=node(List_tree[0])
root.left=node(List_tree[1])
root.right=node(List_tree[2])
print("tree")
print(tree)


def disp_tree(tree):
    if tree:
        print(tree.val)
    
    if tree.left:
        disp_tree(tree.left)
    
    if tree.right:
        disp_tree(tree.right)

print("print the tree")
disp_tree(root)
        

