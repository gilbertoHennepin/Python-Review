class Author:
    def __init__(self, name,):
        self.name = name
        self.books = []

    def __str__(self):
        titles = ', '.join(self.books) or 'No published books'
        return f' Author name: {self.name}. Books: {titles}'

    def publish(self, title):
        self.books.append(title)
    
def main():

        gabriel = Author('Sam')
        gabriel.publish('Goosepumps')
        gabriel.publish('Captain Underpants')
        print(gabriel)

        gil = Author('gil')
        print(gil)

main()






    
    