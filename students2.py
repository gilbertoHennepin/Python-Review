from dataclasses import dataclass

@dataclass
class Student2:
        name: str
        school_id: str
        gpa: float

        def __str__(self):
            return f'Name {self.name}, GPA: {self.gpa}'

def main():
    alex = Student2('Alex', 'abcdef', '2.33')
    print(alex.name)
    print(alex.school_id)
    print(alex)

    sam = Student2('Sam', 'qwerty', '3.38')
    print(sam)

    Lam = Student2('Lam', 'lolol', '4.1')
    print(Lam)
    
main()