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

#is_even
def even(num):
    return num%2==0

#grade_calculate
def grade(marks):
    if marks>90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


#function call
print(greet("Muskan"))

print(greet_student("Muskan"))

marks=[98,56,78,50,99]
high,low,avg=stats(marks)
print(f"Highest marks :{high},lowest marks:{low},average marks :{avg}")

num=89
print(f"is number even :{even(num)}")

print(grade(89))
print(grade(99))

#*args = used when we don't know hoe many arguments we have to pass in function
#1
def info(greeting,*names):
    for name in names:
        print (f"{greeting} {name}")

info("Hello","Muskan","Aayush","Aanya")

#2
def total(*args):
    return sum(args)

print(total(13,15,18,19))

#**kwargs
#1
def greetings(greeting,**details):
    print(f"{greeting} My name is {details["name"]} . I am {details["age"]} years old. I am from {details["college"]}")

greetings("Hello",name="Muskan",age=19,college="LPU")

#2
def profile(**kwargs):
    for key ,value in kwargs.items():
        print(f"{key}: {value}")
profile(name="Muskan",age=19,college="LPU")
