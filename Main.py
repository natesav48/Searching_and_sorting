
def Binary_Search():
    values = (1,12,15,17,190,196,200)
    Target = 17
    MIN = 0
    HIGH = len(values)
    FOUND = False
    ANSWER = 0
    MID = 0

    while (FOUND == False) and (MIN <=HIGH):
        MID = ((MIN + HIGH)//2)
        if values[MID] == Target:
            FOUND = True
            ANSWER = MID
        elif Target > values[MID]:
            MIN = MID + 1
        else:
             HIGH = MID - 1
        print(FOUND, MID)
        if FOUND == True:
            print(Target, "Found as string",ANSWER)
        else:
            print(Target, "was not found")
#Binary_Search()

#BUBBLE SORT
def Bbl_sort():
    lst=[1,4,7,12,5,60]
    for i in range(0,len(lst)):
        for j in range(0,len(lst)-1):
            if lst[j] > lst[j+1]:
                Temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = Temp
    print(lst)
#Bbl_sort()



def sel_sort_failed():
    lst = [1,8,7,21,12,20,10,5]
    min1 = 0
    x = 0
    temp = 0
    for i in range(0,len(lst)-1):
        x = min1
        for j in range(min1+1, len(lst)):
            if lst[j] < lst[x]:
                x = j
                temp = lst[i]
                lst[i] = lst[min1]
                lst[min1] = temp
    print(lst)

sel_sort_failed()


#chat gpt inspired code
def sel_sort():
    lst = [1, 8, 7, 21, 12, 20, 10, 5]
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]

    print(lst)

sel_sort()