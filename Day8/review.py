#사용자로부터 영화 종류를 나타낸 정수 1-3과 나이를 입력받습니다. 각 영화와 가격은 다음과 같이 설정합니다.
#1. 액션영화:10000원
#2. 로맨틱 코미디: 8000dnjs
#3. 공포영화: 9000dnjs
#나이에 따른 할인율은 다음과 같습니다.
#13세미만:50%할인
#60세이상: 30%할인
#사용자의 나이와 선택한 영화에 따라 할인을 적용한 최종 티켓 가격을 계산하여 출력하는 프로그램을 작성하세요.

#movie = {
    #1:{
        #'name':'액션',
        #'price':10000,
    #},
    #2: {
        #'name': '로맨틱',
        #'price': 9000,
    #},
    #3: {
        #'name': '공포',
        #'price': 8000,
    #}
#}

#for i in range(1, len(movie) + 1):
    #print(f"{movie[i]['name']} {movie[i]['price']}")


#movie_choice = int(input("영화를 고르세요"))
#age =int(input("나이를 입력하세요"))

#
#if age >= 60:
    #print(f"{movie[movie_choice]['name']} {movie[movie_choice]['price'] * 0.7}")
#elif age <= 13:
    #print(f"{movie[movie_choice]['name']} {movie[movie_choice]['price'] * 0.5}")
#else:
    #print(f"{movie[movie_choice]['name']} {movie[movie_choice]['price'] * 1}")





#유저에게 영단어를 입력받고 대문화화된 각각의 스펠리이 담긴 리스트 출력

#for i in range('megastudy'):
    #print(i)

#user = input("영단어 임력:")
#word = [i.upper() for i in user]
#print(word)

#threeList = [i for i in range(101) if i % 7 == 0]
#print(threeList)



#word == 'megastudy'
#[i for i in word if i not in 'aeiou']



#threeList = [i for i in range(101) if i % 2 == 0]
#print(threeList)

#어떤 단어에서 모음만 제거한 버스만 입력하면 bs만 나오게


a = [i if i %15 !=0 else '오이' for i in range(101)]

print(a)



