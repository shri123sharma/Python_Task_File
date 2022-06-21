# def get_sequence(l2):
#      from functools import reduce

#      l2=[6,8,7,9, 1112, 1113, 100,101, 102,100, 1001, 1002, 1003, 1111,10]
#      l1 = l2.copy()
#      l1.sort()
#      li1=[]
#     #  import pdb;pdb.set_trace()
#      for i in l1:
#          li = []
#          single_list = []
#          if li1 != []:
#              single_list += reduce(lambda x,y: x+y, li1)
#          if i not in li1 and i not in single_list:
#              if (i not in data for data in li1):
#                  for jn in l1[1:]:       
#                      if i not in li:
#                          li.append(i)
#                      next_item = li[-1]+1
#                      if jn ==  next_item and jn-1 == li[-1] :
#                          li.append(next_item)
#                      else:continue
#                  li1.append(li)
#      return li1
# print(get_sequence([6,7,8,51, 52,1,2,11 ,12, 13, 50,  53]))


# l1=[6,7,8,1,2,3,9,10,11]
# l2=l1.copy()
# l3=[]
# for i in range(0,len(l1)-1):
#     l4=[]
#     if l1[i+1]-l1[i]==1:
#         # a=[l1[i],l1[i+2]]
#         l4.append(l1[i])
#         l3.append(l4)
#         if i not in l4:
#            break
# print(l4)

# # myList = [5, 4, 3, 6, 3, 5, 6, 2, 3, 10, 11, 3]

# # def do_somthing():
#     #your code here
#     pass

# for i in range(len(myList)-4):
#     new_list = myList[i:i+4] #here, using list slicing to jump ahead four elements.
#     if all(new_list[-1] > b for b in new_list[:-1]) and all(new_list[:-1][c] > new_list[:-1][c+1] for c in range(len(new_list)-2)):
#         # print(do_something())
#         pass

# l1=[6,7,8,9,1,2,3,4,9,10,11]
# l2=l1.copy()
# l3=[[l1[i],l1[i+1],l1[i+2]] for i in range(0,len(l1)-2)]
# print(l3)

# l1=[6,7,1,2]
# l1.sort()
# print(len(l1))
# l3=[]
# l4=[]
# # import pdb;pdb.set_trace()
# for i in range(1,len(l1)):
#     print(i)
   
#     if l1[i]-l1[i-1]==1:
#         l3.append(l1[i-1])
        

#     else:
#         l3.append(l1[i-1])
#         l4.append(l3.copy())
#         l3.clear()

#     if i==(len(l1)-1):
#         if l1[i]-l1[i-1]==1:
#             l3.append(l1[i])
#             l4.append(l3.copy())
            
#         else:
#             l3.append(l1[i])
#             l4.append(l3.copy())
#             # l3.clear()
# print(l4)

