with open("Problem_01.txt") as f:
    lines = f.readlines()
data = [number.strip() for number in lines]

master_list = []
summa = 0

for num in data:
    if num != '':
        summa += int(num)
    else:
        master_list.append(summa)
        summa = 0
print(max(master_list))