#---------- Error & Exceptions  in Python -----------------

'''
# enter the word "ten" to see a ValueError msg
x = int(input('Enter a number: '))
x += 20
print(x)


# This will throw a NameError
#print(nonexistant_variable)

# Try-Block Exception to handle errors

try:
    x = int(input('Enter a number: '))
    
except:
    print('That\'s not a valid number')

   

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except:
        print('That\'s not a valid number')

    print('\nAttempted Input')


# If you want code to keep running use a while-loop & 
# break when correct input is entered 

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except:
        print('That\'s not a valid number')

    print('\nAttempted Input')

'''

# The "finally clause  is used to run a code we want to run before try-block
# exit the code 

while True:
    try:
        x = int(input('Enter a number: '))
        break
    # Throw exception  only when wrong input was entered
    except ValueError:
        print('That\'s not a valid number')
    # ctrl + c to leave terminal
    except KeyboardInterrupt:
        print('\no input taken')
        break

    finally:
        print('\nAttempted Input')