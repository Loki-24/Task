def output(input_list):

    series = {j: 0 for j in range(1, 10)}
    for i in input_list:
        for j in range(1, 10):
            if i % j == 0:
                series[j] += 1
    return series
input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
result = output(input_list)
print(result)