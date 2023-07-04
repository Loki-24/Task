# inputs
a = input('Enter first number: ')
b = input('Enter second number: ')
operator = input('Enter operation: ')
# operations between a & b
if operator == "sum":
    result = float(a) + float(b)
elif operator == "sub":
    result = float(a) - (b)
elif operator == "division":
    result = float(a) / float(b)
elif operator == "multiply":
    result = float(a) * float(b)
print ('The Division of {0} and {1} is {2}'.format(a, b, result))
