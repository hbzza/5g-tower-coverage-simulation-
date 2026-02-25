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

dist_range = np.linspace(1, 1000, 400)
signal_line = tower_power - path_loss(dist_range)

plt.figure(figsize=(7,5))
plt.plot(dist_range, signal_line, color='orange')
plt.title("5G Signal Strength vs Distance")
plt.xlabel("Distance from Tower (m)")
plt.ylabel("Signal Strength (dBm)")
plt.grid(True)
plt.show()

users = np.array([10, 50, 100, 200, 300, 400, 500])
latency = 5 + (users ** 1.2) / 50   # Simple congestion model

plt.figure(figsize=(7,5))
plt.plot(users, latency, marker='o', color='green')
plt.title("5G Tower Load vs Latency")
plt.xlabel("Number of Users")
plt.ylabel("Latency (ms)")
plt.grid(True)
plt.show()