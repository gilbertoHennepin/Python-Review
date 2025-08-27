from traceback import print_tb


name = input('Enter your name ')
while not name:
    print('enter at least one character ')
    name = input ('Enter your name ')

month = input('What month where you born in ')
while not month:
    print('enter at least on character ')
    month = input ('What month where you born in ')

print(f'Hello!! {name}')
a = name
print('Letters in your name')
print(len(a))



if ('August') == month:
    print('Happy birthday month')
else:
    print(' not birthday month ')
