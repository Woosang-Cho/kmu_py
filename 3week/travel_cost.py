print('여행 경비 계산기입니다. ')

per_person = float(input('(1/4)개인 경비를 입력하세요(원): '))
share = float(input('(2/4)공동 경비를 입력하세요(원): '))

person = int(input('(3/4)여행 인원수를 입력하세요(명): '))

total_cost = per_person*person + share

rate = float(input('(4/4) 예금의 이율을 입력하세요(%/년): '))

result = float(total_cost/(1 + rate/100)*(1/person))

print(f'각자 입금할 금액은 {round(result, -1): ,.0f} 원 입니다')



