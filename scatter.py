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

#plt.scatter(sw3, script3, color = 'green', marker = 'o')
#plt.scatter(manual3, script3, color = 'blue', marker = 'x')
# plt.scatter(script4, sw4, color = 'blue', marker = 'x')
# plt.scatter(script5, sw5, color = 'purple', marker = 's')

point = (0, 0) 
slope_high = 1.1   
slope_low = 0.9    
# plt.axline(point, slope=slope_low, linestyle='--', color='black')
# plt.axline(point, slope=slope_high, linestyle='--', color='black')

# plt.xlim(9.5, 11)
# plt.ylim(9.5, 11)

# plt.title("Comparison of Estimated Settling Velocity to Ground Truth\nfor 3mm Microplastics")
# plt.ylabel("Object-Detection Model Velocity(cm/s)")
# plt.xlabel("Ground Truth Velocity (cm/s)")

fig, axes = plt.subplots(1,3, figsize = (15,5))

axes[0].scatter(sw3, script3, color = 'green', marker = 'o')
axes[0].scatter(manual3, script3, color = 'blue', marker = 'x')
axes[0].axline(point, slope=slope_low, linestyle='--', color='black')
axes[0].axline(point, slope=slope_high, linestyle='--', color='black')
axes[0].set_xlim(8, 13)
axes[0].set_ylim(8, 13)
axes[0].set_title('3 mm')
axes[0].set_xlabel('Ground Truth')
axes[0].set_ylabel('Object-Detection Model')

axes[1].scatter(sw4, script4, color = 'green', marker = 'o', label = 'Stopwatch Ground Truth')
axes[1].scatter(manual4, script4, color = 'blue', marker = 'x', label = 'Manual Frame Extraction Ground Truth')
axes[1].axline(point, slope=slope_low, linestyle='--', color='black', label = '+-10% error boundary')
axes[1].axline(point, slope=slope_high, linestyle='--', color='black')
axes[1].set_xlim(15, 20)
axes[1].set_ylim(15, 20)
axes[1].set_title('4 mm')
axes[1].set_xlabel('Ground Truth')
axes[1].set_ylabel('Object-Detection Model')

axes[2].scatter(sw5, script5, color = 'green', marker = 'o')
axes[2].scatter(manual5, script5, color = 'blue', marker = 'x')
axes[2].axline(point, slope=slope_low, linestyle='--', color='black')
axes[2].axline(point, slope=slope_high, linestyle='--', color='black')
axes[2].set_xlim(3, 8)
axes[2].set_ylim(3, 8)
axes[2].set_title('5 mm')
axes[2].set_xlabel('Ground Truth')
axes[2].set_ylabel('Object-Detection Model')

axes[1].legend(bbox_to_anchor=(0.5, -0.5), loc='lower center', ncol=2)
plt.suptitle("Comparison of Settling Velocity Estimated by Object-Detection Model to Ground Truths for Different Sizes of Microplastics in cm/s")

plt.tight_layout()

plt.show()