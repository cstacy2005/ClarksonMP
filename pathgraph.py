import csv
import matplotlib.pyplot as plt
import numpy as np

x3mm = []
y3mm = []
with open('videos/StopwatchTest2/3mm_tap_1mp_sw6.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader, None) 
    for row in reader:
        if len(row) > 1: # Ensure the row has enough columns
            x3mm.append(row[2]) 
            y3mm.append(row[3])
    del x3mm[-1]
    del y3mm[-1]

           
for i in range(len(y3mm)):
    y3mm[i] = 640 - float(y3mm[i])

for i in range(len(x3mm)):
    x3mm[i] = float(x3mm[i])

x4mm = []
y4mm = []
with open('videos/StopwatchTest2/4mm_tap_1mp_sw6.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader, None) 
    for row in reader:
        if len(row) > 1: # Ensure the row has enough columns
            x4mm.append(row[2]) 
            y4mm.append(row[3])
    del x4mm[-1]
    del y4mm[-1]
    
for i in range(len(y4mm)):
    y4mm[i] = 640 - float(y4mm[i])

for i in range(len(x4mm)):
    x4mm[i] = float(x4mm[i])
           
x5mm = []
y5mm = []
with open('videos/StopwatchTest2/5mm_tap_1mp_sw6.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader, None) 
    for row in reader:
        if len(row) > 1: # Ensure the row has enough columns
            x5mm.append(row[2]) 
            y5mm.append(row[3])
    del x5mm[-1]
    del y5mm[-1]

for i in range(len(y5mm)):
    y5mm[i] = 640 - float(y5mm[i])

for i in range(len(x5mm)):
    x5mm[i] = float(x5mm[i])

fig, axes = plt.subplots(1,3)

axes[0].scatter(x3mm, y3mm, color = 'blue', marker = '.')
axes[0].set_title('3 mm')
axes[0].set_xlim(0, 480)
axes[0].set_ylim(0, 640)



axes[1].scatter(x4mm, y4mm, color = 'blue', marker = '.')
axes[1].set_title('4 mm')
axes[1].set_xlim(0, 480)
axes[1].set_ylim(0, 640)

axes[2].scatter(x5mm, y5mm, color = 'blue', marker = '.')
axes[2].set_title('5 mm')
axes[2].set_xlim(0, 480)
axes[2].set_ylim(0, 640)


plt.suptitle("Comparison of Settling Velocity Estimated by Object-Detection Model to Ground Truths for Different Sizes of Microplastics in cm/s")

plt.tight_layout()

plt.show()