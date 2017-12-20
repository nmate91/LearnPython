def insertion_sort(numbers):
    for i in range(1,(len(numbers))):
        key = numbers[i]
        j = i - 1
        while (j > -1 and numbers[j] > key):
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers

print(insertion_sort([2, 6, 1, 3, 11, 7, 4]))