#grade calculator
marks=int(input("Enter your marks: "))
if marks>90:
    grade="A"
elif marks >=75:
    grade="B"
elif marks>=60:
    grade="C"
elif marks>=40:
    grade="D"
else:
    grade="F"
print(f"Grades : {grade}")

# FizzBuzz - print numbers 1 to 20
# but for multiples of 3 print "Fizz"
# for multiples of 5 print "Buzz"
# for multiples of both print "FizzBuzz"

for i in range(1,21):
    if i%15==0:
        print("FrizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)