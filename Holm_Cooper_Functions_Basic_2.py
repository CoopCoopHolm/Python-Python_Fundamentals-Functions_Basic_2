# def countdown(num):
#     newList = []
#     for i in range(num, -1, -1):
#         newList.append(i)
#     return newList 
# print(countdown(10))

# def pnr(newList):
#     print(newList[0])
#     return newList[1]
# print(pnr([3,4]))

# def fpl(newList):
#     return newList[0] + len(newList)
# print(fpl([1,2,3,4,5]))

# def vgs(list1):
#     list2 = []
#     if len(list1) < 2:
#         return False   
#     for i in range(len(list1)):
#         if list1[i] > list1[1]:
#             list2.append(list1[i])
#     return list2
# print(vgs([1,2,3,4,5]))

def tltv(length, val):
    newList = []
    for i in range(length):
        newList.append(val)
    return newList
print(tltv(10000,1))