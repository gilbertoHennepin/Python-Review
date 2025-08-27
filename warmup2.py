NumberOfClasses = int(input('How many classes are you takign this semester? '))


ClassesThisSemester = []


for i in range(NumberOfClasses):
    class_name = input(f"Name of Class {i+1}: ")
    ClassesThisSemester.append(class_name)

print("Classes you are taking ")

for i, class_name in enumerate(ClassesThisSemester):
    print(f"{i+1} {class_name}")