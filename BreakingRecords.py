def breaking_records(scores):
    min, max, countMin, countMax = scores[0], scores[0], 0, 0
    for num in scores:
        if num < min:
            countMin += 1
            min = num
        elif num > max:
            countMax += 1
            max = num
    result = [countMax, countMin]
    return result


if __name__ == '__main__':
    scores = [10,5,20,20,4,5,2,25,1]
    print(breaking_records(scores))
    scores2 = [3,4,21,36,10,28,35,5,24,42]
    print(breaking_records(scores2))
