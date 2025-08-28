NumberOfClasses = int(input('How many classes are you takign this semester? ')) # get user input


ClassesThisSemester = [] # empty list


for i in range(NumberOfClasses): # iterate throguh # of classes and add class
    class_name = input(f"Name of Class {i+1}: ")
    ClassesThisSemester.append(class_name)

print("Classes you are taking ")

for i, class_name in enumerate(ClassesThisSemester): # print classes 
    print(f"{i+1} {class_name}")
