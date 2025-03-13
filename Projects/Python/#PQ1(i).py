#PQ1(i)
def Sort(num_list, target):
    sorted_list = sorted(num_list)
    low = 0
    high = len(sorted_list) -1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] < target:
            low = mid + 1
        elif sorted_list[mid] > target:
            high = mid - 1
        else:
            return num_list.index(target)
        return -1
    
#Example
numbers = [4,8,12,16,20,24,28,32] 
target_number = 4
print(Sort(numbers,target_number))      