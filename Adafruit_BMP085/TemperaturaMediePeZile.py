from collections import defaultdict

tempzi = defaultdict(list)
current_day = None
total =0
c = 0
with open("rezultate_bmp.txt", 'r') as f:
    for line in f:
        if line[:4] == 'data':
            current_day = line.split()[2]
        elif 'Temperature' in line:
            temp = float(line.split()[1])
            total += temp
            c += 1
            tempzi[current_day].append(temp)
for day, temps in tempzi.items():
    avg_temp = sum(temps) / len(temps)
    print(f'temperatura medie in ziua {day} este {avg_temp:.2f}')