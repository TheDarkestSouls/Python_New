count = 0

str1 = input()
str2 = input()

for i in range(len(str1) - (len(str2) - 1)):
    if str2 == str1[i:i+len(str2)]:
        count += 1


print(f"Вторая строка входит в первую {count} раз(а).")