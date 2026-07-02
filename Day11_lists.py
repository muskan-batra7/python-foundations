#lists and list methods

#basic operations
mylist=[98,68,84,56,99,97]
students=["Muskan","Aayush","Sanvi"]
marks=[78,89,56,98,45,45]
bts=["RM","Jin","suga","Jhope","Jimin","V","jungkook"]
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

marks.sort()              #sort in ascending order
print(marks)
marks.sort(reverse=True) #sort in descending order
bts.sort(key=str.lower)    #sort after doing lower method
bts.reverse()              #reverse the list
print(bts)

print(marks)
print(marks.count(45))     #count how mant 45 present in the list
print(bts.index("Jin"))    #find index of "Jin"

#loop through list
for x in bts:
    print(x)

for i in range(len(bts)):
    print(bts[i])
    
y=0
while(y<len(bts)):
    print(bts[y])
    y+=1

#function with loop
marks2=[88,87,91,77,72,94]
def getstat(marks2):
    return {
        "Total": sum(marks2),
        "Average": sum(marks2)/len(marks2),
        "Highest": max(marks2),
        "Lowest": min(marks2),
        "Passed":len(list(filter(lambda x: x>=40,marks2)))
    }
stats=getstat(marks2)
for key , value in stats.items():
    print(f"{key}: {value}")


