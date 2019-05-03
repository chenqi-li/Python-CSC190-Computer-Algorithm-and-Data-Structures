def selection_sort(u):
    #Find last element in PQ
    last = len(u)-1

    while(last>0):
        #Find smallest
        largest = 0
        for i in range(0,last+1,1):
            if u[i] > u[largest]:
                largest = i

        #Swap smallest and last
        temp = u[largest]
        u[largest] = u[i]
        u[i] = temp

        #Reduce last
        last -= 1
    return True



def heapify(u):
    heap = []

    for i in range(0,len(u),1):
        heap += [u[i]]
        x = i

        while(x>0):
            if heap[int((x-1)/2)] < heap[x]:
                temp = heap[x]
                heap[x] = heap[int((x-1)/2)]
                heap[int((x-1)/2)] = temp
            x = int((x-1)/2)

    for j in range(0,len(u),1):
        u[j] = heap[j]

    return True



def reheapify(u,end):
    heap = []

    for i in range(0, end, 1):
        heap += [u[i]]
        x = i

        while (x > 0):
            if heap[int((x - 1) / 2)] < heap[x]:
                temp = heap[x]
                heap[x] = heap[int((x - 1) / 2)]
                heap[int((x - 1) / 2)] = temp
            x = int((x - 1) / 2)


    for j in range(0, end, 1):
        u[j] = heap[j]

    return True



def heap_sort(u):
    end = len(u)-1

    heapify(u)
    while (end>0):
        temp = u[0]
        u[0] = u[end]
        u[end] = temp
        reheapify(u,end)
        end -= 1

    return True



def merge_sort(u):
    if len(u) <= 1:
        return True
    else:
        left_lst = list(u[0:int(len(u)/2)])
        right_lst = list(u[int(len(u)/2):len(u)])

        merge_sort(left_lst)
        merge_sort(right_lst)

        index = 0
        l = 0
        r = 0

        while l < len(left_lst) and r < len(right_lst):
            if left_lst[l] < right_lst[r]:
                u[index] = left_lst[l]
                l+=1
            else:
                u[index] = right_lst[r]
                r+=1
            index += 1

        while l < len(left_lst):
            u[index] = left_lst[l]
            index += 1
            l += 1
            r += 1

        while r < len(right_lst):
            u[index] = right_lst[r]
            index += 1
            l += 1
            r += 1


def countingSort(arr, exp1):
    n = len(arr)

    output = [0] * (n)

    count = [0] * (10)

    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int((index) % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int((index) % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    max1 = max(arr)

    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10





v1=[10,9,8,7,6,5,4,3,2,1,0]
v2=[100,1,1000,9,8,7,2,2000,10]
v3=[100,10,1000,9,8,7,2,6,5,2,3,1]

for i in [ v1,v2,v3 ]:

   x=list(i)
   merge_sort(x)
   print(x)

   x=list(i)
   selection_sort(x)
   print(x)

   x = list(i)
   selection_sort(x)
   print(x)

   x = list(i)
   heap_sort(x)
   print(x)
