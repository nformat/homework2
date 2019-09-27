a = input("Введите любую строку: \n")

if a == "":
    print("Ничего не введено!!!")
elif a.isdigit():
    print("\nЭто число!\n")
else:
    print("Это не число!\nВ строке пробелов:", a.count(" "), "\nВ строке точек:",a.count("."))

b = "Homework"
b = b.center(100, " ")
print(b)

print(a.title())
