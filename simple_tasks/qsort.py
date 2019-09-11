def qsort(li):
    if len(li) < 2:
        return li
    n = li.pop(len(li) // 2)
    left = [i for i in li if i < n]
    right = [i for i in li if i >= n]
    return qsort(left) + [n] + qsort(right)


def msort(li):
    def merge(li1, li2):
        li3 = []
        i, j = 0, 0
        while i < len(li1) and j < len(li2):
            if li1[i] < li2[j]:
                li3.append(li1[i])
                i += 1
            else:
                li3.append(li2[j])
                j += 1
        return li3 + li1[i:] + li2[j:]

    if len(li) < 2:
        return li
    return merge(msort(li[:len(li)//2]), msort(li[len(li)//2:]))


print(qsort([1, 4, 1, 2,5,43,324,234,4,32,434]))
print(msort([1, 4, 1, 2,5,43,324,234,4,32,434, 2, 3,3,2,2,2]))