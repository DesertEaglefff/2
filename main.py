n = int(input())
m = int(input())
x = input()
if x == '-' :
    print(n-m)
elif x == '+':
    print(n+m)
elif x == '/' and m !=0:
    print(n / m)
elif x == '*':
    print(n * m)
elif x == 'mod':
    print(n % m)
elif x == 'div' and m !=0:
    print(n // m)
elif x == 'pow':
    print(n ** m)
elif x == 'div' or x == '/' and m == 0:
    print('На ноль делить нельзя!')
else:
    print('Ошибка')


