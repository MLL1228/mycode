def insertSort( arr ):
    length = len(arr)
    for i in range(1, length):
        x = arr[i]
        for j in range(i, -1, -1):
            # j为当前位置，试探j-1位置
            # 如果当前数较小，插入到前面
            if x < arr[j-1]:
                print(j, arr[j-1])
                arr[j] = arr[j-1]

            else:
                # 位置确定为j
                break

        arr[j] = x
        print(arr)

def printArr(arr):
    for item in arr:
        print(item)
arr = [4, 3, 7 ,8 ,4 , 4 ,5]
insertSort(arr)
# printArr(arr)
print(arr)

#
# def inertsort(l):  #参数的传入，当想传入的是一个list时，直接传入一个变量就行了
#     N=len(l)
#     for x in range(1,N):
#         a,b=x,x
#         n=l[x]
#         while n<l[a-1] and a-1>=0:
#             a=a-1
#             if a-1<0:
#                 a=0
#         while b>a:
#             l[b]=l[b-1]
#             b=b-1
#         l[a]=n
#
# l=[1,3,2,8,5,3,1]
# inertsort(l)
# print (l)

