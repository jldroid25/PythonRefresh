
#-----Use a stack to decode the the hidden message ------
import Stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
S = Stack.Stack()

# Your solution Here
#S.push(string)

while S.is_empty():
    S.push(string)
    S.peek()
    print(S.peek())



print(reversed_string)