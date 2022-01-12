def plus_minus(arr):
    count_p, count_n, count_z = 0, 0, 0
    for num in arr:
        if num < 0:
            count_n += 1
        elif num == 0:
            count_z += 1
        elif num > 0:
            count_p += 1
    pos = float(count_p) / float(len(arr))
    print('%.6f' % pos)
    neg = float(count_n) / float(len(arr))
    print('%.6f' % neg)
    zero = float(count_z) / float(len(arr))
    print('%6f' % zero)


if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]
    plus_minus(arr)
