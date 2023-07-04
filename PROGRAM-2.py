def series(a):
    output = []
    for i in range(1, a+1):
        output.append(2*i -1)
    return output
a = int(input("Enter a number: "))
result = series(a)
print(result)
