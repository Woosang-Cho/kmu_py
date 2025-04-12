# 입력 유효성 체크
def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        print(f"잘못된 입력입니다. {', '.join(valid_options).upper()} 중에서 선택해주세요.")

# 피자 가격 계산
def calculate_cost(size, add_pepperoni, add_cheese):
    size_cost = {"s": 13000, "m": 17000, "l": 20000}
    pepperoni_cost = 2000 if size == "s" else 3000
    cheese_cost = 1000

    cost = size_cost[size]
    if add_pepperoni == "y":
        cost += pepperoni_cost
    if add_cheese == "y":
        cost += cheese_cost
    return cost

print("\n 안녕하세요. 민지킴의 피자마을입니다. ^_^ \n")

# 입력 받기
flavor = get_valid_input("피자 맛을 선택하세요(치즈/불고기/새우): \n", ["치즈", "불고기", "새우"])
size = get_valid_input("사이즈를 선택하세요(S/M/L): \n", ["s", "m", "l"])
pepperoni = get_valid_input("페퍼로니를 추가하시겠습니까? (y/n) \n", ["y", "n"])
cheese = get_valid_input("치즈를 추가하시겠습니까? (y/n) \n", ["y", "n"])

# 가격 계산
total_cost = calculate_cost(size, pepperoni, cheese)

print(f"\n선택하신 피자는 {flavor}맛입니다.")
print(f"결제 금액은 {total_cost:,}원 입니다.")