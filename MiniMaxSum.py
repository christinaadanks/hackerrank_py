def miniMaxSum(arr):
    min, max, sum, temp = 0, 0, 0, 0
    for i in range(0, len(arr)):
        temp += arr[i]
    sum = temp
    for j in range(0, len(arr)):
        sum -= arr[j]
        if min == 0:
            min = sum
        if sum > max:
            max = sum
        if sum < min:
            min = sum
        sum = temp
    print(min, max)

if __name__ == '__main__':
    arr = [256741038, 623958417, 467905213, 714532089, 938071625]
    miniMaxSum(arr)
