'''
BMI 지수를 계산하는 계산기입니다.
BMI 지수는 체중(kg)과 신장(cm)으로, 다음과 같이 계산됩니다:

BMI = 체중 / (신장**2)
'''
def func_BMI():
    weight = float(input("Enter the Weight(kg): "))
    height_m = float(input("Enter the Height(cm): "))
    height_cm = height_m*(1/100)
    return weight,height_cm

weight, height_cm = func_BMI()

BMI = weight / (height_cm * height_cm)

print(f"\nBMI: {BMI:.2f}")

if BMI < 18.5:
    print('저체중')
elif 18.5 <= BMI < 23:
    print('정상')
elif 23 <= BMI < 25:
    print('비만 전 단계 (과체중 or 위험 체중)')
elif 25 <= BMI < 30:
    print('1단계 비만')
elif 30 <= BMI < 35:
    print('2단계 비만')
else:
    print('3단계 비만')
