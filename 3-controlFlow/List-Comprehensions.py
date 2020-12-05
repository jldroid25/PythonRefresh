'''
In Python, you can create lists really quickly and concisely with list comprehensions. 
This example from earlier:

capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())

#can be reduced to:

capitalized_cities = [city.title() for city in cities]


List comprehensions allow us to create a list using a for loop in one step.

You create a list comprehension with brackets [], 

including an expression to evaluate for each element in an iterable. 
This list comprehension above calls city.title() for each element city in cities, 
to create each element in the new list, capitalized_cities.

------------Conditionals in List Comprehensions
You can also add conditionals to list comprehensions (listcomps). 
After the iterable, you can use the if keyword to check a condition in each iteration.

squares = [x**2 for x in range(9) if x % 2 == 0]

The code above sets squares equal to the list [0, 4, 16, 36, 64], 
as x to the power of 2 is only evaluated if x is even. 

If you want to add an else, you will get a "syntax error" doing this.
squares = [x**2 for x in range(9) if x % 2 == 0 else x + 3]

- Instead: If you would like to add else, you have to move the conditionals 
to the beginning of the listcomp, right after the expression, like this.
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]

FYI:List comprehensions are not found in other languages, but are very common in Python.

'''
print("\n\n")


squares = [ x**2 for x in range(9)]
print(squares)

# Can also add if-statement to check condition of each iteration, check for "even"

squares = [ x**2 for x in range(9) if x % 2 == 0]
print("\n")


print(squares)

# ----------------More List-Comprehension practices 

# Extract first name from a list.
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_name = [name.split()[0].lower() for name in names]
print(first_name)

print("\n")

# Find Multiples of Three in a list of numbers
multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)

print("\n")

#Filter Names by Scores 65 & higher
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in  scores.items() if score >= 65]
print(passed)

print("\n\n")