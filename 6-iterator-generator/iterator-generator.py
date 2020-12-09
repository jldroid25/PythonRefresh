import numpy as np
'''
--Iterators And Generators

- Iterables: are objects that can return one of their elements at a time, 
such as a list. Many of the built-in functions we’ve used so far, 
like 'enumerate,' return an iterator.

- An iterator: is an object that represents a "stream of data". 
This is different from a list, which is also an iterable, 
but is not an iterator because it is not a stream of data.

- Generators are a simple way to create iterators using functions. 
You can also define iterators using classes, 
which you can read more about 

Here is an example of a generator function called my_range, 
which produces an iterator that is a stream of numbers from 0 to (x - 1).
'''

def my_range(x):
    i = 0
    while i < x:
        #Yield is a generator , allow function to generate one value at a time
        yield i
        i += 1

'''
Notice that instead of using the return keyword, it uses yield. 
This allows the function to return values one at a time, and start 
where it left off each time it’s called. 
This yield keyword is what differentiates a generator from a typical function.

Remember, since this returns an iterator, we can convert it to a list 
or iterate through it in a loop to view its contents. For example, this code:
'''

for x in my_range(5):
    print(x)

'''

Why Generators?

Generators are a lazy way to build iterables. 
They are useful when the fully realized list would not fit in memory, 
or when the cost to calculate each list element is high and you 
want to do it as late as possible. But they can only be iterated over once.


'''

# Quiz Implement my_enumerate
lessons = [
    "Why Python Programming", "Data Types and Operators", 
    "Control Flow", "Functions", "Scripting"
    ]

def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

print('\n')

# write a chunker 
def chunker(iterable, size):
    
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))        

print('\n')

# Same as above but much simplier
def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

for chunk2 in chunks(range(30), 4):
    print(list(chunk2))


# see numpy (as np) import above file
lst = range(50)
print(np.array_split(lst, 5))

'''
--Generator Expressions
Here's a cool concept that combines generators and list comprehensions! 
You can actually create a generator in the same way you'd normally write a 
list comprehension, except with parentheses instead of square brackets.
 For example:

'''
sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares
