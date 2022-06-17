# s="xxooxoxoo"

# print(s[0],s[1],s[2])
# print(s[3],s[4],s[5])
# print(s[6],s[7],s[8])

# r1,r2,r3=(s[0],s[1],s[2]),(s[3],s[4],s[5]),(s[6],s[7],s[8])
# c1,c2,c3=(s[0],s[3],s[6]),(s[1],s[4],s[7]),(s[2],s[5],s[8])
# p1,p2=(s[0],s[4],s[8]),(s[2],s[4],s[6])

# t=0
# a=0
# y=""

# if abs(s.count("x")-s.count("o"))>1:
#     a+=1
    
 
# if(r1==('x', 'x', 'x') or r2==('x', 'x', 'x') or r3==('x', 'x', 'x') c1==('x', 'x', 'x') or c2==('x', 'x', 'x') or c3==('x', 'x', 'x') or p1==('x', 'x', 'x') or p2==('x', 'x', 'x')):
#     t+=1
#     y="x"
    


# if(r1==('o', 'o', 'o')or r2==('o', 'o', 'o') or r3==('o', 'o', 'o') or c1==('o', 'o', 'o') or c2==('o', 'o', 'o') or c3==('o', 'o', 'o') or p1==('o', 'o', 'o') or p2==('o', 'o', 'o')):
#     t+=1
#     y='o'

# if (t==2 or a==1):
#     print("Its impossible")
#     exit()
    
# if y=="x" and t==1:
#     print("X Win")
# if y=="o" and t==1:
#     print("O win")

# elif "_" in s and t==0:
#     print("game incomplete")
# else:
#     print("draw")

# accept_range = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     player1=player2 = ''
#     while player1 not in accept_range:
#         player1 = int(input('Player 1: Pick a number 1 through 9 on your keypad to put an X on the board: '))
#     while player2 not in accept_range:
#         player2 = int(input('Player 1: Pick a number 1 through 9 on your keypad to put an O on the board: '))

#     print(player2)

# s="123456789"

# s1=set()

# print(s[0],s[1],s[2])
# print(s[3],s[4],s[5])
# print(s[6],s[7],s[8])

# for i in range(len(s)):
#     if i%2!=0:
#         # for j in range(len(s)):
#         n=int(input("x term "))
#         if n not in s1:
#             s1.add(n)
#             s=s.replace(s[n-1],"x")
            
#         else:
#             while(n in s1):
#                 n=int(input("please enter a valid term"))
#             s=s.replace(s[n-1],"x")
            
#     else:
#         n=int(input("o term "))
#         if n not in s1:
#             s1.add((n))
#             s=s.replace(s[n-1],"o")
#         else:
#             while(n in s1):
#                 n=int(input("please enter a valid term"))
#             s=s.replace(s[n-1],"o")
            
            

#     print(s[0],s[1],s[2])
#     print(s[3],s[4],s[5])
#     print(s[6],s[7],s[8])

#     r1,r2,r3=(s[0],s[1],s[2]),(s[3],s[4],s[5]),(s[6],s[7],s[8])
#     c1,c2,c3=(s[0],s[3],s[6]),(s[1],s[4],s[7]),(s[2],s[5],s[8])
#     d1,d2=(s[0],s[4],s[8]),(s[2],s[4],s[6])

#     t=0
#     a=0
#     y=""

#     if abs(s.count("x")-s.count("o"))>1:
#         a+=1

#     if r1==('x', 'x', 'x') or r2==('x', 'x', 'x')or r3==('x', 'x', 'x') or c1==('x', 'x', 'x') or c2==('x', 'x', 'x') or c3==('x', 'x', 'x') or d1==('x', 'x', 'x') or d2==('x', 'x', 'x'):
#         t+=1
#         y="x"

#     if r1==("o","o","o") or r2==("o","o","o") or r3==("o","o","o") or c1==('o', 'o', 'o') or c2==('o', 'o', 'o') or c3==('o', 'o', 'o') or d1==('o', 'o', 'o') or d2==('o', 'o', 'o'):
#         t+=1
#         y="o"

#     if (t==2 or a==1):
#         print("Its impossible")

#     if t==1 and y=="x":
#         print("X win")
#         break

#     if t==1 and y=="o":
#         print("O win")
#         break

#     elif ("_" in s or t==0):
#         continue
        
#     else:
#         print("Draw")
# if ("_" in s or t==0):
#     print("Game Incomplete")
a = 10