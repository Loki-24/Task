def series(a):
    output = []
    for i in range(1, a+3):
        if i%2!=0:
            output.append(i)
    return output

a = int(input("Enter a number: "))
output = series(a)
print(output)
