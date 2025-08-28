


class Student:
    def __init__(self, name, school_id, gpa): #define students class
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

    def __str__(self): #set up the way info is goign to be printed
        return f'Student name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}'
        
alex = Student('Alex', 'abcdef', '2.33') #define student
print(alex.name)
print(alex.school_id)
print(alex)

sam = Student('Sam', 'qwerty', '3.38')#define student
print(sam) #display info 

Lam = Student('Lam', 'lolol', '4.1')#define student
print(Lam)#display info 
