def selection_sort(numbers):
    for i in range(0, len(numbers)):
        largest = numbers[i]
        for j in range(i, len(numbers)):
            if largest < numbers[j]:
                largest = numbers[j]
        numbers.remove(largest)
        numbers.insert(0, largest)
    return numbers

if __name__ == "__main__":
    print(selection_sort([2, 6, 1, 3, 11, 7, 4]))