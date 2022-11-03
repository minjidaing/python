# a = int(input("팩토리얼을  입력하세요 : "))
# j = 1
# for item in range(1, a+1, 1):
#     j *= item    
# print(j)

# a=int(input())
# def ab(n):
#     if(n>1):
#         return n*ab(n-1)
#     else:
#         return 1
# print(ab(a))



# def abc(x,y):
#     if(x<99):
#         print(x , y ,end=' ')
#         x=x+y
#         y=y+x
#         return abc(x,y)
#     else:
#         return 1
# abc(int(input()),int(input()))

# n=int(input())

# def hanoi(n,rood1,rood3,rood2):
#     if n == 1:
#         print(rood1,rood2)

#     else:
#         hanoi(n-1,rood1,rood2,rood3)
#         print(rood1,rood2)
#         hanoi(n-1,rood2,rood3,rood1)

# print(n**2 -2)
# hanoi(n,1,3,2)


#클래스
# class Human:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
# areum=Human('아무개',40,'남자')
# print(areum.age)

# class human:
#     def abc(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
    
#     def zzz(self):
#         print("이름:{},나이{},성별{}",format(self.name,self.age,self.sex))


# class Student:
#     def start(self):
#         print('안녕하세요')
#     def printName(self,name):
#         print('이름은 {0} 입니다'.format(name))

# stu=Student()
# Student.start(stu)
# stu.printName('홍길동')

# class Student:
#     schoolName='Korea'
#     schoolname='USA'
#     schoolnamme='Japan'

# stu1=Student()
# stu2=Student()

# print('stu1의 주소:{0}'.format(id(stu1)))
# print('stu2의 주소:{0}'.format(id(stu2)))



# # Student.schoolName='Seoul'

# print("\nStudent의 학교:",Student.schoolName)
# print("\nstu1의 학교:",stu1.schoolname)
# print("\nstu2의 학교:",stu2.schoolnamme)


# x=1
# try:
#     print(x)
# except:
#     print("error")
# finally:
#     print("done")


# try:
#     a=[1,2]
#         print(a[3])
# except:
#     print("error")

# a = 10

# if a == 10:
#     pass
# else:
#     print('틀림')


# class gugudan:
#     def gugu():
#         for i in range (1,10):
#             for j in range (2,10):
     
    
#                 print(f'{i} * {j} = {i*j}')
#                 print (" ")


# minji = gugudan.gugu()
# print(minji)


#클래스 함수로 구구단
# class gugu:
#     def data(self):
#         self=0
#     def gugudan(self):
#         for i in range(2,10):
#             for j in range(1,10):
#                 print(f'{i}*{j}={i*j}')
#                 print(" ")
# b=gugu()
# b.gugudan()


# class kkk:
#     def abc():
#          for i in range(2,10):
#             for j in range(1,10):
#                 print(f'{i} X {j} = {i*j}')
#             print(" ")


# aaa = kkk.abc()
# print(aaa)


class aa:
    def jjakhol():
        num1=int(input("숫자입력"))
        if num1%2==0:
            print(num1,"짝수입니다.")
        else:
            print(num1,"홀수입니다.")
    def average():
        num1=int(input("숫자입력"))
        num2=int(input("숫자입력"))
        print((num1+num2)/2)
        
    def square():
        for i in range(1,5):
            for j in range(1,3):
                print("*",end='')
            print('')

# b=aa.jjakhol()
aa.jjakhol()
aa.average()
aa.square()


# a=int(input())
# for i in range(1,10):
#     print(f'{i}+{a}={i+a}')
                