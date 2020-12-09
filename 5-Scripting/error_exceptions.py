#---------- Error & Exceptions  in Python -----------------

'''
# enter the word "ten" to see a ValueError msg
x = int(input('Enter a number: '))
x += 20
print(x)

'''
# This will throw a NameError
#print(nonexistant_variable)

# Try-Block Exception to handle errors

try:
    x = int(input('Enter a number: '))
except:
    print('That\'s not a valid number')


