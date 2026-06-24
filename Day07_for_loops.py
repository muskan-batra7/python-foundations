#highest and lowest marks using for loop
marks=["89","67","98","65","43"]
highest=marks[0]
lowest =marks[0]
for x in marks:
    if x>highest:
        highest=x
    if x<lowest:
        lowest =x
print(f"Highest marks : {highest}")
print(f"Lowest marks: {lowest}")

#range() using for loop
for i in range(2,30,3):
    print (i)

#for loop iterate through string
for j in "Muskan":
    print(j)

#break
for k in marks:
    if k=="98":
        break
    print(k)

#continue
for l in  marks :
    if l=="98":
        continue
    print(l)

#nested loop

name=["Muskan","Aayush","Sanvi"]
surname =["Batra","Mohindru","Sharma"]
for y in name:
    for z in surname:
        print(y,z)