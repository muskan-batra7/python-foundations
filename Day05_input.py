#user input
height=float(input("Enter your height: "))
weight=float(input("Enter your weight: "))
bmi= weight / (height ** 2)
print(f"BMI= {bmi:.2f}")
if bmi<18.5:
    category = "underweight"
elif bmi<25:
    category="Normal weight"
elif bmi<30:
    category="Overweight"
else:
    category ="Obese"
print(f"Category = {category}")

#type conversion 
age ="19"
age=int(age)  #convert str type to int 
print(type(age))
age =float(age)   #convert int type to float
print(type(age))