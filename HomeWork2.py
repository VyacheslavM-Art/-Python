# Задание 1

mylist= [15,"story", 27.7,[1,2,4]]
for i in mylist:
    print(type(i))
# Задание 2
llist=[]
lenlist=int(input("Введите длину листа:"))
for i in range(lenlist):
#    llist.append(i)
    llist.append(input("Введите {} элемент: ".format(i)))

print("Первичный лист : ", llist)
if lenlist % 2 == 1:
    lenlist=lenlist-1
for i in range(0,lenlist,2):
    j=llist[i]
    llist[i]=llist[i+1]
    llist[i + 1]=j
print("Лист после обработки: ", llist)

# Задание 3

mount=int(input("Введите месяц в виде числа от 1 до 12:"))
my_dict={1:"Зима", 12:"Зима", 2:"Зима", 3:"Весна", 4:"Весна", 5:"Весна", 6: "Лето",7: "Лето",8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень" }
print("(Dict)Это время года:",my_dict.get(mount))
mylist=["Зима", "Весна", "Лето", "Осень"]
if mount==1 or mount == 2 or mount == 12:
    print("(List)Это время года:", mylist[0])
elif mount > 2 and mount <6:
    print("(List)Это время года:", mylist[1])
elif mount > 2 and mount <6:
    print("(List)Это время года:", mylist[2])
else:
    print("(List)Это время года:", mylist[3])

# Задание 4
s=input("Введите текст: ")
mylist=s.split()
for i in range(len(mylist)):
    if len(mylist[i])>10:
        print(i," : ",mylist[i][:10])
    else:
        print(i, ":", mylist[i])
# Задание 5
my_list = [7, 5, 3, 3, 2]
print("Начальный рейтинг:", my_list)
a=int(input("Введите натуральное число : "))
my_list.append(a)
my_list.sort(reverse=True)
print("После добавления:", my_list)

# Задание 6
count = int(input("Введите кол-во товаров: "))
my_list=[]
for i in range(1,count+1):
    print("Товар №", i)
    my_dict={"название": input("Название товара №{}: ".format(i)), "цена":input("Цена товара №{}: ".format(i)), "количество": input("Количество товара №{}: ".format(i)),"eд":input("Единица измерения товара №{}: ".format(i))}
    my_list.append((i,my_dict))

print(my_list)
my_dict= my_list[0][1]
for i in my_dict.keys():
    my_dict[i]=[my_dict[i]]
for i in range(1,len(my_list)):
    print(type(my_list[i][1]))
    for j in my_list[i][1].keys():
        for ij in range(len(my_dict[j])):
            if my_dict[j][ij] != (my_list[i][1][j]):
                my_dict[j].append(my_list[i][1][j])

print(my_dict)