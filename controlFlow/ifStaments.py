
# If-statements run or skip a code base on weather a condition is true or false
bank_balance = 20
phone_balance = 4

print(phone_balance, bank_balance)

# here we have if-statement, condition, follow by colon 
#  This is is a boolean expression that evaluate to either true or false
if phone_balance < 5: 
    #block of code to execute if condition is true
      phone_balance += 10
      # or execute this one if false
      bank_balance -= 10

print(phone_balance, bank_balance)

