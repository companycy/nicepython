import math

QUEEN = 8
INITVAL = -1

def init():
    """"""
    arr = [INITVAL] * QUEEN
    return arr

def printout(arr):
    """"""
    print arr
    print '\n'

def valid(arr, row, col):
    """"""
    if row < 0 or col < 0:
        return False
    # col_dup = col in arr[0, row]
    for i in range(0, row):
        if col == arr[i] or math.fabs(row-i) == math.fabs(col-arr[i]):
            return False
    else:
        return True

def queen(arr):
    """"""
    cnt, row, col = 0, 0, 0
    while row < QUEEN:
        while col < QUEEN:
            if valid(arr, row, col):
                # print row, ' and ', col
                arr[row] = col
                col = 0
                break
            else:
                col = col+1

        if arr[row] == INITVAL:
            if row == 0:
                break           # fail this time
            else:
                row = row-1
                col = arr[row]+1 # restart from col+1
                arr[row] = INITVAL
                continue

        if row == QUEEN-1:      # it can be else if other than if
            cnt = cnt + 1
            print 'a kind of solution'
            printout(arr)
            col = arr[row]+1
            arr[row] = INITVAL    # try next col
            continue

        row = row+1

    print cnt

if __name__ == '__main__':
    """"""
    arr = init()
    print arr
    queen(arr)
    print arr
