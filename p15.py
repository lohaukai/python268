Height = eval(input())
Weight = eval(input())
BMI = Weight/((Height/100)**2)
Comment = ['Underweight', 'Normal', 'Overweight', 'Obese Class I', 'Obese Class II', 'Obese Class III']
if BMI < 18.5:
    print('%.2f' %BMI)
    print(Comment[0])
elif 18.5<=BMI<24:
    print('%.2f' %BMI)
    print(Comment[1])
elif 24<=BMI<27:
    print('%.2f' %BMI)
    print(Comment[2])
elif 27<=BMI<30:
    print('%.2f' %BMI)
    print(Comment[3])
elif 30<=BMI<35:
    print('%.2f' %BMI)
    print(Comment[4])
else:
    print('%.2f' %BMI)
    print(Comment[5])
