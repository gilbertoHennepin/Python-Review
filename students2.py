from dataclasses import dataclass

@dataclass
class Student2:
        name: str #define annotations
        school_id: str
        gpa: float

        def __str__(self): #set up how info will be printed 
            return f'Name {self.name}, GPA: {self.gpa}'

def main(): #def main
    alex = Student2('Alex', 'abcdef', '2.33') #define student
    print(alex.name)
    print(alex.school_id)
    print(alex)

    sam = Student2('Sam', 'qwerty', '3.38') #define student
    print(sam)

    Lam = Student2('Lam', 'lolol', '4.1')#define student 
    print(Lam)
    
main() # call main method 
