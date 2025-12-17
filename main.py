import numpy as np
import matplotlib.pyplot as plt

tower_x, tower_y = 0, 0        
frequency = 3.5e9              
tower_power = 40                  
grid_size = 200                


def path_loss(distance_m): 
    distance_km = distance_m / 1000 
     
    distance_km = np.where(distance_km == 0, 0.001, distance_km) 
    loss = 128.1 + 37.6 * np.log10(distance_km) 
    return loss

x = np.linspace(-500, 500, grid_size)
y = np.linspace(-500, 500, grid_size)
xx, yy = np.meshgrid(x, y)


distance = np.sqrt((xx - tower_x)**2 + (yy - tower_y)**2)
signal_strength = tower_power - path_loss(distance)


plt.figure(figsize=(7, 6))
plt.imshow(signal_strength, extent=(-500, 500, -500, 500), origin='lower', cmap='viridis')
plt.colorbar(label="Signal Strength (dBm)")
plt.title("5G Tower Coverage Heatmap")
plt.xlabel("Distance X (m)")
plt.ylabel("Distance Y (m)")
plt.show()