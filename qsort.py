
import sys
import random

lenth = 10

def partition(arr, left, right):
    """get pivot index"""
    pivot_index, pivot = left, arr[left]
    arr[left], arr[right] = arr[right], arr[left]
    for i in range(left, right+1):
        if arr[i] < pivot:
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
            pivot_index = pivot_index+1
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    return pivot_index

def qsort(arr, left, right):
    """qsort of in-place version"""
    if left >= right:
        return
    pivot_index = partition(arr, left, right)
    qsort(arr, left, pivot_index-1)
    qsort(arr, pivot_index+1, right)
    # print arr

def init():
    """init array"""
    arr = []
    sys.setrecursionlimit(100000)
    for i in range(lenth):
        arr.append(random.randint(0,1000))
    return arr

if __name__ == '__main__':
    arr = init()
    print 'before qsort: ', arr
    qsort(arr, 0, len(arr)-1)
    print 'after qsort: ', arr
