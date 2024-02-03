####짝수번째 애들만 골라라

#def get_even_items(list):
  #"""짝수번째 애들을 반환합니다."""
  #return [item for i, item in enumerate(list) if i % 2 == 1]


#list = [1, 2, 3, 4, 5]
#print(get_even_items(list))


#제일 작은 수를 리턴해라.


#def solution(numList):
    #if len(numList) ==1:
        #return [-1]
    #else:
        #numList.remove(min(numList))
        #return numList
#print(solution([4,1,2,3]))


#####숫자로만 되어있으면 트루 문자 섞여 있으면 거짓
def solution(string):
    if string.isdigit():
        return True
    else:
        return False






def is_numeric(string):
  """문자열이 숫자로만 이루어져 있으면 True, 그렇지 않으면 False."""
  for char in string:
    if not char.isdigit():
      return False
  return True


string = "1234"
print(is_numeric(string))  # True

string = "a1234"
print(is_numeric(string))  # False






