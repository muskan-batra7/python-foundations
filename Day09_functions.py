#functions
#basic
def greet(name):
    return f"Hello {name}"

#default argument
def greet_student(name,college="LPU"):
    return f"Hello {name} from {college}"

#multiple return values
def stats(marks):
    return max(marks),min(marks),sum(marks)/len(marks)

#function call
print(greet("Muskan"))

print(greet_student("Muskan"))

marks=[98,56,78,50,99]
high,low,avg=stats(marks)
print(f"Highest marks :{high},lowest marks:{low},average marks :{avg}")
