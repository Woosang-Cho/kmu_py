# 필요한 정보 입력받기
per_person_cost = float(input("1인당 경비를 입력하세요: "))
shared_cost = float(input("공동 경비를 입력하세요: "))
num_people = int(input("여행 인원을 입력하세요: "))
interest_rate = float(input("예금 이율(%)을 입력하세요: ")) / 100

# 총 경비 계산
total_cost = (per_person_cost * num_people) + shared_cost

# 개인 부담 계산
shared_per_person = shared_cost / num_people
final_per_person_cost = per_person_cost + shared_per_person

# 이율 반영 금액 계산
deposit_per_person = final_per_person_cost * (1 + interest_rate)

# 결과 출력
print("\n여행 경비 계산 결과:")
print(f"총 경비: {total_cost:.2f} 원")
print(f"1인당 부담 금액: {final_per_person_cost:.2f} 원")
print(f"이율 반영 후 각자 입금할 금액: {deposit_per_person:.2f} 원")

