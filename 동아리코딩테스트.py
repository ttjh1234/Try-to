# -*- coding: utf-8 -*-
#7기 멤버 코딩테스트 문제
#문제1 
#중간고사. 기말고사, 과제 점수를 모두 합한 10명의 학생의 점수를 
#구하는 코드를 zip을 이용하여 점수가 높은 순서대로 정렬하시오.
중간고사=[34,30,26,40,33,15,31,21,17,40]
기말고사=[45,48,25,50,50,28,39,33,47,42]
과제=[5,10,8,10,7,7,9,10,2]
list1=[]
for x,y,z in zip(중간고사,기말고사,과제):
    list1.append(x+y+z)
list1.sort(reverse=True)
list1    
#문제2
#비타민에서는 동아리 지원시 개별 지원번호가 부여된다.
#지원번호를 입력하면 성별, 기수, 편입여부, 운영진여부 를 출력하는 프로그램을 작성하시오.
#지원번호는 앞에서 부터 순서대로 합격시 활동시작연도 -활동시작학기(1학기,2학기)- 성별(1- 편입아니고 남자,2- 편입아니고 여자, 3-편입이고 남자, 4-편입이고 여자)-임의 부여번호2자리 - 운영진 여부(운영진이면 s)
#비타민은 18년도 1학기부터 시작되었다. (1기)
#예) 21-1-1-37-s 1학기 남자 (-는 이해를 돕기위해 추가한 예시)
sn=input('지원번호를 입력하시오 : ')
def print1(sn):
    if sn[:2]=='18':
        if sn[2]=='1':
            기수='1'
        else: 기수='2'
    if sn[:2]=='19':
        if sn[2]=='1':
            기수='3'
        else: 기수='4'
    if sn[:2]=='20':
        if sn[2]=='1':
            기수='5'
        else: 기수='6'
    if sn[:2]=='21':
        if sn[2]=='1':
            기수='7'
        else: 기수='8'        
    if sn[3]=='1':
        성별='남'
        편입='x'
    elif sn[3]=='3':
        성별='남'
        편입='o'
    elif sn[3]=='2':
        성별='여'
        편입='x'
    elif sn[3]=='4':
        성별='여'
        편입='o'
    if len(sn)==7:
        운영진='o'
    else: 운영진='x'
    print('성별:',성별)
    print('기수:',기수)
    print('편입:',편입)
    print('운영진:',운영진)        
print1(sn)

#문제3        
import pandas as pd
import numpy as np

#문제3-1 titanic.csv를 불러와 titanic에 저장하시오.
titanic=pd.read_csv('./titanic.csv')
print(titanic.head())
#문제3-2 titanic에서 Pclass, Age, Fare 열을 index 0부터 100까지 뽑아 df에 저장하시오.
# (loc ,iloc 둘 중 적어도 하나 사용)
df=titanic[['Pclass','Age','Fare']].iloc[:101]
print(df)

#문제3-3 df에서 pclass 열을 버리고 버려졌는지 df를 불러서 확인하시오.
df.drop('Pclass',axis=1,inplace=True)
print(df.head())

#문제3-4 df의 열별로 결측치가 몇개 존재하는지 확인하시오.
print(df.isnull().sum(axis=0))
#문제3-5 결측치가 있다면 그 다음 데이터로 채우시오.(index 숫자가 더 큰 = 다음)
df.Age.fillna(method='bfill',inplace=True)

#문제3-6 df에서 Age가 40 이상인 행을 모두 뽑고 Age가 내림차순으로 정렬되도록 
#데이터프레임을 구성하시오.(데이터프레임에는 Age열과 Fare열이 모두 있어야함)
df=df[df['Age']>=40]
df=df.sort_values(by='Age',ascending=False)
print(df.head())

#문제3-7 df.Fare를 평균이 0이고 분산이 1인 가우시안 정규분포를 가진 값으로 
# 변환하려하는데 표준화하는 수식을 코드로 작성하고 lambda를 이용하여 
# df의 Fare 열을 표준화하시오.

def normalize(x):
    return (x-x.mean())/x.std()

df.Fare=df[['Fare']].apply(lambda x : normalize(x))

#문제3-8 itanic에서 Name에서 first name만을 뽑아 
#새로운 열인 First_Name을 titanic에 추가하시오.

#참고 : johann + Sebastian + Bach
#(First name) +(Middle name) + (Surname)
titanic['First_Name']=titanic['Name'].str.split(',').str[0]

print(titanic.head())
