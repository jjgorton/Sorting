# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
# ------- This didn't work well once larger lists were combined
    # if arrA[0] < arrB[0]:
    #     merged_arr = arrA + arrB
    # else:
    #     merge_sort(arrA + arrB)

# --------- This got a lot closer, but still didn't completely sort
    # merged_arr = arrA + arrB
    # for i in range(len(merged_arr)-1):
    #     if merged_arr[i] > merged_arr[i+1]:
    #         merged_arr[i], merged_arr[i+1] = merged_arr[i+1], merged_arr[i]

# --------- Got the idea to do a single loop through both lists simultaneously from https://www.geeksforgeeks.org/merge-sort/

    # i = j = k = 0

    # tempList = []

    # while i < len(arrA) and j < len(arrB):
    #     if arrA[i] < arrB[j]:
    #         # merged_arr[k] = arrA[i]
    #         # merged_arr[k+1] = arrB[j]
    #         tempList.append(arrA[i])
    #         i += 1
    #     else:
    #         # merged_arr[k] = arrB[j]
    #         # merged_arr[k+1] = arrA[i]
    #         tempList.append(arrB[j])
    #         j += 1

    #     k += 1
    #     print(f'in while {tempList}')

##--------- Combining some ideas into something that works
    tempList = []
    while len(arrA) > 0 or len(arrB) > 0:
        if len(arrA) == 0:
            tempList += arrB
            arrB = []
        elif len(arrB) == 0:
            tempList += arrA
            arrA = []
        else:
            if arrA[0] < arrB[0]:
                tempList.append(arrA.pop(0))
            else:
                tempList.append(arrB.pop(0))

    merged_arr = tempList
    print(merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        arrA = merge_sort([arr[num] for num in range(0, len(arr)//2)])
        arrB = merge_sort([arr[num] for num in range(len(arr)//2, len(arr))])

        # print(f'arrA is {arrA}\n arrB is {arrB}')

        return merge(arrA, arrB)
        # return merge(merge_sort(arrA), merge_sort(arrB))

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
