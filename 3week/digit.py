num = int(input('두 자리 양의 정수를 입력하세요: '))

tens = num // 10
ones = num % 10

result = tens + ones 

print(f"{tens} + {ones} = {result}")
