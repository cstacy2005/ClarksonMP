import matplotlib.pyplot as plt
import numpy as np

sw3 = [9.655, 9.929, 10.108, 10, 9.825]
script3 = [10.603, 10.879, 10.728, 10.720, 10.716]
manual3 = [10.562, 10.782, 10.707, 10.712, 10.634]
sw4 = [15.135, 15.556, 15.301, 15.385, 16.279]
script4 = [18.243, 17.160, 19.568, 17.150, 16.684]
manual4 = [16.509, 16.687, 16.509, 16.509, 16.509]
sw5 = [6.264, 4.754, 5.395, 5.263, 5.726]
script5 = [6.636, 4.979, 5.848, 5.562, 5.924]
manual5 = [6.627, 5.015, 5.783, 5.484, 5.913]

all_3mm_data = [script3, sw3, manual3]
all_4mm_data = [script4, sw4, manual4]
all_5mm_data = [script5, sw5, manual5]

# plt.boxplot(all_data, labels=['Dataset 1', 'Dataset 2', 'Dataset 3'])

# plt.title('Side-by-Side Boxplots of Multiple Datasets')
# plt.ylabel('Values')

fig, axes = plt.subplots(1,3, figsize = (15,5))

axes[0].boxplot(all_3mm_data, labels=['Model', 'Stopwatch', 'Frame Extraction'])
axes[0].set_title('3 mm')
axes[0].set_xlabel('Calculation Method')
axes[0].set_ylabel('Settling Velocity (cm/s)')
axes[0].set_ylim(8, 13)
axes[1].boxplot(all_4mm_data, labels=['Model', 'Stopwatch', 'Frame Extraction'])
axes[1].set_title('4 mm')
axes[1].set_xlabel('Calculation Method')
axes[1].set_ylabel('Settling Velocity (cm/s)')
axes[1].set_ylim(15, 20)
axes[2].boxplot(all_5mm_data, labels=['Model', 'Stopwatch', 'Frame Extraction'])
axes[2].set_title('5 mm')
axes[2].set_xlabel('Calculation Method')
axes[2].set_ylabel('Settling Velocity (cm/s)')
axes[2].set_ylim(3, 8)

plt.suptitle("Comparison of Settling Velocity Estimated by Object-Detection Model to Ground Truths for Different Sizes of Microplastics")

plt.tight_layout()

plt.show()