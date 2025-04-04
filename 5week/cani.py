age = int(input('나이를 입력하세요: '))
height = float(input('키(cm)를 입력하세요: '))

if age>=10 and height>=120:
    print('탑승 가능')
elif age<10 and height>=140:
    print('보호자 동반 탑승 가능')
else:
    print('탑승 불가')