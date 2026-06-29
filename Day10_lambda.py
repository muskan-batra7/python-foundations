# Day 10 - lambda, map, filter

#normal function vs lambda
def double(n):
    return n*2
print(double(4))  #8 is answer

x=lambda n:n*2
print(x(4))     #8 is answer

#lambda with multiple arguments
add =lambda x,y:x+y
print(add(3,4))    #7

#lambda in condition
grade=lambda marks:"Pass" if marks>=60 else "Fail"
print(grade(34))  #fail
print(grade(98))  #pass


#map function with lambda
#1
numbers=[1,2,3,4,5]
doubled=list(map(lambda z:z*2,numbers))  #double every number in string
print(doubled)

#2
marks=[89,56,80,56]
grades=list(map(lambda x:"Pass" if x>=60 else "Fail",marks))
print(grades)

#filter function using lambda
#1
odd_num=list(filter(lambda x:x%2!=0,numbers)) 
#filters out all numbers which does not satisfies the condition(filters out even numbers)
print(odd_num)

#2
passed=list(filter(lambda x: x>=60,marks))
print(passed)

#sorted function using lambda
#1
words=["apple","Cherries","Banana","guavas"]
sorted_fruits=sorted(words,key=lambda x:len(x)) #sort list by length of fruits (strings)
print(sorted_fruits)

#2
students=[
    {"name":"Muskan","marks":92},
    {"name":"Sanvi","marks":78},
    {"name":"Aayush","marks":91}
]
sorted_students=sorted(students,key=lambda x:x["marks"],reverse=True)
for s in sorted_students:
    print(f"{s["name"]}: {s["marks"]}")

