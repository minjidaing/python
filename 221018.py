# a=10
# b=20
# c=a+b
# print(c)




# a=12*3
# b=12*4
# if a > b:
#     print('a')
# else:
#      print('b')




# a=70
# if a>=90 :
#     print('A')
# elif 80<=a<90 :
#     print('B')
# elif 70<=a<80 :
#     print('C')
# elif 60<=a<70 :
#     print('d')
# elif 50<=a<60 :
#     print('F')




# num=1
# while num<=100:
#         print(num)
#         num = num + 1




# n = int(input('어쩌고저쩌고: '))
# num=1
# sum=0
# while(num<=n):
#     sum+=num
#     num+=1
# print(sum)





# def abc(a,b): //사칙연산
#     print(f'{a} 더하기 {b}={a+b}')
#     print(f'{a} 빼기 {b}={a-b}')
#     print(f'{a} 나누기 {b}={a/b}')
#     print(f'{a} 곱하기 {b}={a*b}')

# abc(5,10)



# a=int(input('입력주세요:')) //곱셈

# for n in range(1,10):
#     print(f'{a}*{n}={a*n}')

# a=int (input('입력해:'))

# for n in range(1,10):
#     print(f'{a}*{n}={a*n:2d}')
    

# import pyautogui
# import keyboard
# import time

# while 1:
#     position = pyautogui.position()
#     # if keyboard.is_pressed('enter'):
#     print(position)
        
#     position = pyautogui.doubleClick(x = 1303 , y =1000)
#     time.sleep(0.5)
#     position = pyautogui.click(x = 2339 , y =435)
#     time.sleep(0.5)



# for i in range(5):  별찍기
#     for j in range(5):
#         print('*',end='')
#     print()




# for n in range(2,10):  구구단
#     for a in range(1,10):
#         print(f'{n}*{a}={a*n}')
#     print()


# for i in range(5):  별로 삼각형
#     for j in range(i+1):
#         print('*',end="")
#     print('')


# a=8  삼각형
# for i in range(a):
#     print(""*(a+1-i),end="")
#     print("*"*(i+1))





# a = 5 피라미드
# for i in range(a):
#     print(' '*((a -1)-i), end = '')
#     print('*'*((2*i)-1))



#     for i in range(a//2-1): 역피라미드
#     print(' ' * (i + 1), end = "")
#     print('*' * ((a//2*2)-3-2*i))




# for i in range(0,5): 피라미드
#     for j in range(5-i):
#         print(' ',end="")
#     for j in range(i*2-1):
#         print('*',end="")
#     print('')




# for i in range(0,5): 역피라미드
#     for j in range(0,i):
#         print(' ',end='')
#     for j in range(i,9-i): 
#         print('*',end='')
#     print('  ')


# 2차 배열

# print("before")
# a = [[1, 2, 3],[4, 5, 6]]

# for b in range(2):
#     for c in range(3):
#         print(f'{a[b][c]}')


# print("구구단을 외우자 구구단을 외우자")
# a = [1, 2, 3 ,4 , 5, 6, 7, 8, 9]

# for i in range(1,9): 
#     for j in range(1,9):
#         print(f'{a[i]}*{a[j]}={a[i]*a[j]}')


# time = 121
# a=time//60
# b=time%60
# print(a,'시간',b,'분') 

# f=75
# c=(f-32)/1.8
# print(c)



# mile=5
# km=round(mile/0.623137,5)
# meter=round(1000*km,2)
# print(mile,'마일\n',km,'킬로미터\n',meter,'미터')




# a="eat work play sleep repeat"
# b=a.replace(a,"working playing")
# print(b)
 



