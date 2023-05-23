#this is my shopping list

# shoplist=['apple','mango','carrot','banana']
# print('I have',len(shoplist),'items to purchase.')
# print('These items are:')
# for item in shoplist:
#     print(item)
# print('\nI also have to buy rice.')
# shoplist.append('rice')
# print('My shopping list is now ',shoplist)
# print('I will sort my list now')
# shoplist.sort()
# print('Sorted shopping list is ',shoplist)
# print('The first item I will buy is',shoplist[0])
# olditem=shoplist[0]
# del shoplist[0]
# print('I bought the ',olditem)
# print('My shopping list is now ',shoplist)

#리스트 추가 예제
# heroes=[]
# heroes.append("아이언맨")
# heroes.append("닥터 스트레인지")
# print(heroes)

# 리스트 항목 접근하기

# letters=['A','B','C','D','E']
# print(letters[0])
# print(letters[1])
# print(letters[2])

# 슬라이싱

# letters=['A','B','C','D','E','F']
# print(letters[0:3])
# print(letters[3:])
# print(letters[:])

# 리스트 항목 변경

# heroes=["아이언맨","토르","헐크","스칼렛 위치"]
# heroes[1]="닥터 스트레인지"
# print(heroes)

# 함수를 이용하여 추가

# heroes.append("스파이더맨")
# print(heroes)
# heroes.insert(1,"배트맨")
# print(heroes)

# 항목 삭제하기

# heroes.remove("스칼렛 위치")
# print(heroes)
# del heroes[0]
# print(heroes)
# last_hero=heroes.pop()
# print(last_hero)
# print(heroes)

# 리스트 탐색하기
# print(heroes.index("헐크"))

# if"슈퍼맨"in heroes:
#     heroes.remove("슈퍼맨")

# 리스트 방문하기

# for hero in heroes:
#     print(hero)

#리스트 정렬하기
# heroes.sort()
# print(heroes)

#Tkinter의 위젯들

# from tkinter import *
# root=Tk()
# root.mainloop()

# 예제: 간단한 다이얼로그
# from tkinter import *

# root = Tk()
# label = Label(root,text="Test")
# label.pack()
# textbox=Entry(root)
# textbox.pack()
# button=Button(root,text="Click")
# button.pack()
# root.mainloop()

#버튼 Widget

# from tkinter import *
# root=Tk()
# button=Button(root,text="Click")
# button.pack()
# root.mainloop()

#버튼 이벤트 처리

# from tkinter import*
# def Button_Clicked():
#     print("황명원입니다")
 
# root=Tk()
# button=Button(root,text="Click",command=Button_Clicked())
# button.pack()
# root.mainloop()
