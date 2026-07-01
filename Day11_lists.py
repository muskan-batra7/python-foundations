#lists and list methods

#basic operations
mylist=[98,68,84,56,99,97]
students=["Muskan","Aayush","Sanvi"]
print(mylist[0])      #first item
print(mylist[-1])     #last item
print(mylist[1:3])    #[68, 84]
print(mylist[-4:-1])  #[84, 56, 99]
print(len(mylist))    #length

#list methods
mylist.insert(2,78)   #insert 78 at 2 index
mylist.append(59)     #insert 59 at last of list
mylist.extend(students) #insert all elememts of students in mylist
mylist.remove(98)        #remove 98
mylist.pop(4)            #remove element at 4 index
del mylist[1]            #remove element at index 1
students.clear()         #remove all elements of list studdnts
seclist=mylist.copy()    #copy all elements of mylist to seclist
mylist=mylist+seclist
marks=[78,89,56,98,45]
marks.sort()              #sort in ascending order
print(marks)
marks.sort(reverse="True") #sort in descending order
print(marks)
print(seclist)
print(mylist)
print(students)