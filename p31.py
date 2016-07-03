Num1 = eval(input())
Num2 = eval(input())
operator = input()

if operator == '+':
    print("%.2f"%Num1, operator, "%.2f"%Num2, "= %.2f"%(Num1+Num2))
elif operator == '-':
    print("%.2f"%Num1, operator, "%.2f"%Num2, "= %.2f"%(Num1-Num2))
elif operator == '/':
    print("%.2f"%Num1, operator, "%.2f"%Num2, "= %.2f"%(Num1/Num2))
elif operator == '*':
    print("%.2f"%Num1, operator, "%.2f"%Num2, "= %.2f"%(Num1*Num2))
