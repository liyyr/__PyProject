listA = ['a','b','c','d','e','f','g','h','i']

def list_div(list, n):
    outList = []
    inList = []

    for index, listStr in enumerate(list, 1):
        if index%n != 0:
            inList.append(listStr)
        else:
            inList.append(listStr)
            outList.append(inList)
            inList = []
            continue

    if inList:
        outList.append(inList)

    return outList

if __name__ == '__main__':
    print(list_div(listA, 4))
