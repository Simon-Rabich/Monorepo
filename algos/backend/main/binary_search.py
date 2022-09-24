def binary_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binary_search(alist[:midpoint], item)
            else:
                return binary_search(alist[midpoint + 1:], item)


def binary_search_iterative_way(blist, target):
    l = 0
    h = len(blist) - 1
    while l <= h:
        mid = (l + h) // 2
        if blist[mid] == target:
            return True
        if blist[mid] > target:
            h = mid - 1
        else:
            l = mid + 1
    return False


if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(binary_search_iterative_way(testlist, 3))
    print(binary_search_iterative_way(testlist, 13))
    #
    # testlist_2 = [0, 3, 5, 9, 10]
    # print(binary_search(testlist_2, 9))
