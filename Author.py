class Author: # define author
    def __init__(self, name,):
        self.name = name
        self.books = []

    
    def __str__(self): # see if theres titles in the list and set up how info will be displayed 
        titles = ', '.join(self.books) or 'No published books'
        return f' Author name: {self.name}. Books: {titles}'

    def publish(self, title): #defiine and add titles to publish method
        self.books.append(title)
    
def main():
        #create author objects 
        gabriel = Author('Sam')
        gabriel.publish('Goosepumps')
        gabriel.publish('Captain Underpants')
        print(gabriel)

        gil = Author('gil')
        print(gil)

main() # call main method 






    
    
