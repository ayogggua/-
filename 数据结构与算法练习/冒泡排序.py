def bulbsort(l):
    length = len(l)
    i = -1
    j = length - 1
    flag = True
    while(i<length-1 and flag):
        i+=1
        flag = False
        while(j>i):
            if l[j-1] > l[j]:
                l[j],l[j-1] = l[j-1],l[j]
                flag = True
            j = j-1
            
    return l


def main():
    test = [1,5,5,6,7,8,9,10,8,10]
    result = bulbsort(test)
    print(result)

main()