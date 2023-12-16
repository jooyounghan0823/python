# 당신의 이름은 무엇입니까?
# 당신은지금 무엇을드시고 싶으십니까?
# 당신은 집에 갈때 어떤 커피를 사실 건가요?
# 당신은 집까지 얼마나 걸리시나요?

# ~~~님은집까지 ~~시간이 걸리시군요, 가시는 집에 ~~를사고, ~~ 커피를 테이크아웃을 하시며
# 집에 가시겠군요.



name = input("당신의 이름은:")
print(f"내 이름은 {name}이다")


food = input("너가 먹고싶은 거는:")
print(f"내가 먹고싶은거는 {food}이다")


coffee = input("집에갈때 어떤커피삼:")
print(f"내가 집에갈때 사는커피는 {coffee}이다")


howlong = input("집까지 얼마나 걸림:")
print(f"집까지 걸리는시간은 {howlong}이다")

print(f"""name은 집까지 {howlong} 시간이 걸리시군요, 가시는 길에 {food}를 사고, {coffee}커피를 테이크아웃하시며 집에 가시겠군요""")
print(f"""{name}은 집까지 {howlong} 시간이 걸리시군요, 가시는 길에 {food}를 사고, {coffee}커피를 테이크아웃하시며 집에 가시겠군요""")


mnu = input("서브웨이에서 뭘 고름:")
print (f"서브웨이에서 먹을 거는 {menu} 이다")

product = input("올리브영에서 뭐살거임:")
print (f"올리브영에서 살거는 {product}이다")


subway = input("서브웨이에서 어떤 메뉴를 고를건가요?")
print(f"{subway} 메뉴는 정말 맛있죠!")
