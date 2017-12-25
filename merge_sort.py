def merge(left_numbers, right_numbers):
    if not len(left_numbers) or not len(right_numbers):
        return left_numbers or right_numbers
    result = []
    i, j = 0, 0
    while len(result) < (len(left_numbers) + len(right_numbers)):
        if left_numbers[i] < right_numbers[j]:
            result.append(left_numbers[i])
            i += 1
        else:
            result.append(right_numbers[j])
            j += 1
        if i == len(left_numbers) or j == len(right_numbers):
            result.extend(left_numbers[i:] or right_numbers[j:])
            break
    return result

def merge_sort(numbers):
    if len(numbers) < 2:
        return numbers
    middle = int(len(numbers) / 2)
    left_numbers = merge_sort(numbers[:middle])
    right_numbers = merge_sort(numbers[middle:])
    return merge(left_numbers, right_numbers)
    
if __name__ == "__main__":
    print (merge_sort([3, 4, 5, 1, 2, 8, 3, 7, 6]))