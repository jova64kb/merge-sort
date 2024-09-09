def merge(left, right):
    res = []
    while 0 < min(len(left), len(right)):
        if left[0] > right[0]:
            res.append(right.pop(0))
        elif left[0] <= right[0]:
            res.append(left.pop(0))
    if 0 < len(left):
        for item in left:
            res.append(item)
    if 0 < len(right):
        for item in right:
            res.append(item)
    return res

def merge_sort(arr):
    if 1 < len(arr):
        len_floor = len(arr) // 2
        left = merge_sort(arr[:len_floor])
        right = merge_sort(arr[len_floor:])
        return merge(left, right)
    else:
        return arr

