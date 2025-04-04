print("\n 안녕하세요. 닥터 노의 봉하마을 피자집입니다. \n")

size = input("사이즈를 선택하세요(S/M/L): \n").lower

if size == "s":
    cost_size = 10000
elif size == "m":
    cost_size = 15000
else:
    cost_size = 20000


pepperoni = input("페퍼로니를 추가하시겠습니까? (y/n) \n").lower

if pepperoni == "y":
    if size == "S":
        cost_size += 2000
    else:
        cost_size += 3000
else:
    cost_size

cheese = input("치즈를 추가하시겠습니까? (y/n) \n").lower

if cheese == "y":
    cost_size += 1000
else:
    cost_size

cost = cost_size

print(f"결제 금액은 {cost}원 입니다.")
