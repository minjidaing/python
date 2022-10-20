# def abc():
#     num_a=int(input('입력:'))
# # num_b=int(input('입력:'))

# # num_a, num_b = map(int, input("두 수를 입력 : ").split())
#     if (num_a<0):
#         print(num_a,"음수")
#     else:
#         print(num_a,"양수")

# abc()





# a=int(input("입력:"))
# b=int(input("입력:"))
# if(a==b):
#     print("두수가 같습니다")
# elif(a<b):
#     print("첫번째 수가 두번째 수보다 작습니다")
# elif(a>b):
#     print("첫번째 수가 두번째 수보다 큽니다")






# do=input(":: ")
# if do =="LOOK":
#     print("모래 둑이 있는 도랑에 갇혔습니다.")
#     print("왼쪽(LEFT)이나 오른쪽(RINGT)으로 엉금엉금 기어갑니다.")
#     do = input(":: ")
#     if do =="LEFT":
#         print("도랑 밖으로 기어 나왔습니다. 배가 있네요!")
#         print("살아 남았습니다!")
#     elif do =="RIGHT":
#         print("아! 둑을 올라갈 수가 없습니다. 오른쪽 둑은 아주 미끄럽습니다.")
#         print("멀리 미끄러져 내려가 이상한 동굴로 떨어졌습니다.")
#         print("살아남지 못했습니다 :( ")
# else:
#     print("대문자로 표시된 동작만 입력해 주십시오.")
#     print("다시 한번 도전해 보십시오!")






# a=int(input("입력"))
# for a in range(a):
#     print("안녕")






# def cc(): 조건에 맞는 수
#     aaa = 0
#     for a in range(1,101):
#         if(a%2==0):
#             if(a%6==0):
#                 aaa += 1
        
#     print(aaa)

# cc()



# def aa():
# aa=int(input("입력:"))

# for d in range(aa,1,-1):

#     print("파이썬 책",d, "권이 들어 있는 책장에 파이썬 책이",d,"권"
# "책을 한권 꺼내 돌려 보고 나니",d,"권이 남았네" )















# a=int(input("입력:"))
# name=
# for a in range():
#     print("안녕 ",)


# array=[273,32,103,"문자열",True,False]
# print(array)
# [273,32,'문자열',True,False]
# print(array[5])





# list_a=[1,2,3]
# list_b=[4,5,6]
# print('# 리스트')
# print("list_a=",list_a)
# print("list_b",list_b)
# print()


# list_a=[1,2,3]
# print("#리스트 뒤에 요소 추가하기")
# list_a.append(4)



# number=[273,103,5,32,65,9,72,800,99]
# for i in range(9):
#     if number[i]%2==1:
#         print(number[i],"는 홀수입니다.")
#     elif number[i]%2==0:
#         print(number[i],"는 짝수입니다.")




# number=["273","103","5","32","65","9","72","800","99"] 자릿수
# for number in (number):
#     print(len(number))



# I=["273","103","5","32","65","9","72","800","99"] 자릿수
# for I in I :
#     print(I,"는",len(I),"자릿수입니다.")
    # ,"는",len(i),"자릿수입니다."





# list_of_list=[[1,2,3],[4,5,6,7],[8,9]]
# for list_

# dict_b={"director":["안소니루소,조루소"],"cast":["아이언맨","노스"]}

# print(dict_b["director"])



# character = {
#     "name" :"기사",
#     "level": 12,
#     "items":{"sword":"불꽃의 검","armor":"풀플레이트"},
#     "skill":["베기","세게베기","아주세게베기"]}
# for key in character:   
#     {
#     print(key,":",character[key])
#     }


# character = {
#     "name": "기사",
#     "level": 12,
#     "items": {
#         "sword": "불꽃의 검",
#         "amor": "풀플레이트"
#     },
#     "skill": ["베기", "세게 베기", "아주 세게  베기"]
# }

# for key in character:
#     if type(character[key]) is dict:
#         for k in character[key]:
#             print('{} : {}'.format(k, character[key][k]) )
#     elif type(character[key]) is list:
#         for item in character[key]:
#             print('{} : {}'.format(key,item))
#     else:
#         print('{} : {}'.format(key,character[key]))



# def a(b,d):
#     return b+d,b-d,b*d

# c=a(10,5)

# print(c)    


# def power(item):
#     return item*item
# def under_3(item):
#     return item<3
# list_input_a=[1,2,3,4,5]

# output_a=map(power,list_input_a)
# print("#map() 함수의 실행결과")
# print("map(power,list_input_a):",output_a)
# print("map(power,list_input_a):",list(output_a))
# print()

# output_b=filter(under_3,list_input_a)
# print("#filter()함수의 실행결과")\
# print("filter(under_3,list_input_a):",output_b)
# print("filter(under_3,list_input_a):",list(output_b))


# file=open("basic.txt","w")
# file.write("Hello Python Programming...!")
# file.close()