name="Muskan Batra"
age=19
college="Lovely professional university"
sgpa=9.326789
branch="CSE-AI and ML"
hobby="Drawing"
tenth_percentage=95.6
#%method
print("Hello,my name is %s"%name)
print("I am %i years old"%age)
#format method
print("I am a student of {} at {}".format(branch,college))
print("My hobby is {}".format(hobby))
#f string method
print(f"My sgpa in first sem was {sgpa:.2f}")
print(f"I scored {tenth_percentage:.2f} in class 10th ")
#string methods
print(len(name))
print("university" in college)
print(f"Surname: {name[7:12]}")
print(name.upper())
print(name.lower())
print(name.strip()) #remove whitespaces
print(name.split(","))
print(hobby.replace("Drawing","Painting"))
print(name.find("B"))
print(college+" -"+ branch)
print(name.center(20,"."))
print(name.capitalize())
print(name.title()) #captilize string of each word
print(name.casefold())   #each  ch lowercase
print(college.endswith("university"))  #return boolean 
print(name.encode())
print(name.swapcase())
table=str.maketrans("btr","123")
print(name.translate(table))
print(" ".join(["Muskan","Batra"]))
print(name.count("a"))
full_name = "Muskan,Batra"
print(full_name.split(","))   # ['Muskan', 'Batra']
sentence = "I love python"
print(sentence.split())       # ['I', 'love', 'python']


