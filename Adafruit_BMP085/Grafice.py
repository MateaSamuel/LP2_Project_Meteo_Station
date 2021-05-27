import matplotlib.pyplot as plt
import numpy as np

def temperatura():
    with open("rezultate_bmp.txt", 'r') as f:
        temps = []
        for line in f:
            if "Temperature" not in line: continue
            temp = line.split(" ")[1]
            temps.append(temp)
    return temps

def altitudine():
    with open("rezultate_bmp.txt", 'r') as f:
        alti = []
        for line in f:
            if "Altitude" not in line: continue
            altitudine = line.split(" ")[4]
            alti.append(altitudine)
    return alti
alti=altitudine()
plt.title("Altitudine")
plt.bar(x=np.arange(len(alti)),height=alti)
plt.show()
temps=temperatura()
plt.title("temperatura")
plt.bar(x=np.arange(len(temps)),height=temps)
plt.show()

