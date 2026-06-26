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
