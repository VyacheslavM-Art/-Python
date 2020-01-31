# задание 1, функция
def div(x,y):
    if y==0:
        return "Ошибка деления на 0"
    elif not x.isdigit() or not y.isdigit():
        return "Ошибка, Введите числа"
    else:
        return float(x)/float(y)
# задание 2, функция
def st(name_user,surname_user, year_bd, email, phone):
    print(f"Name: {name_user}, surname: {surname_user}, year of birth: {year_bd}, e-mail: {email}, phone: {phone}")

# Задание 3, функция
def sum_max(x1,x2,x3):
    return x1+x2+x3-min(x1,x2,x3)

# Задание 4, функция
def my_func(x, y):
    if y>=0:
       return "Error"
    res=1
    for i in range(abs(y)):
        res=res*x
    return 1/res

def my_func_1(x, y):
    if y >= 0:
        return "Error"
    return x**y

# Задание 5, функция
def SumS(s):
    a=[]
    su=0
    a=s.split()
    for i in a:
        if i.isdigit():
            su=su+int(i)
    return su

# Задание 6, функция
def int_func(s):
    return s.title()


# задание 1
print("Результат деления:",div(input("Введите частное: "),input("Введите делитель: ")))

#задание 2
st(name_user="John",surname_user="Smit",year_bd=1990,email="jsmit@xxx.com",phone=8902666666)

#задание 3
print(sum_max(-12,-10,12))

#задание 4
print(my_func(5,-5))
print(my_func_1(5,-5))

# задание 5
ss=0
while True:
    s=input('Введите числа через пробел (для выхода введите Q): ')
    ss=ss + SumS(s)
    print("Сумма равна =",ss)
    if s.find("Q") != -1:
        break

# задание 6
s=input("Введите текст с пробелом: \n")
a=s.split()
s1=""
for i in a:
    s1=s1+int_func(i)+" "
print(s1)

