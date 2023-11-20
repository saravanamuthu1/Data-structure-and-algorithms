def merge_sort(unssorted_array):
    if len(unssorted_array) > 1:
        middle_len = len(unssorted_array) // 2
        left_array = unssorted_array[:middle_len]
        right_array = unssorted_array[middle_len:]
        merge_sort(left_array)
        merge_sort(right_array)
        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
            print(left_array[i],right_array[j])
            if left_array[i] < right_array[j]:
                unssorted_array[k] = left_array[i]
                i=i+1
            else:
                unssorted_array[k] = right_array[j]
                j=j+1
            k+=1
        while i < len(left_array):
            unssorted_array[k] = left_array[i]
            i=i+1
            k=k+1
        while j < len(right_array):
            unssorted_array[k] = right_array[j]
            j=j+1
            k=k+1
        print(unssorted_array)
if __name__ == "__main__":
    merge_sort([5,7,3,10,8,1,2])